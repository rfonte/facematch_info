import importlib
import sys
import types
import numpy as np


class DummyLogger:
    def __init__(self):
        self.infos = []
        self.errors = []
        self.warnings = []

    def info(self, msg):
        self.infos.append(msg)

    def error(self, msg):
        self.errors.append(msg)

    def warning(self, msg):
        self.warnings.append(msg)


class DummyCaptureNotOpened:
    def __init__(self, *_):
        pass

    def isOpened(self):
        return False

    def read(self):
        return False, None

    def release(self):
        pass


class DummyCaptureSingleFrame:
    def __init__(self, *_):
        self._called = 0

    def isOpened(self):
        return True

    def read(self):
        self._called += 1
        frame = np.zeros((100, 100, 3), dtype=np.uint8)
        return True, frame

    def release(self):
        pass


def reload_main_with_patches(monkeypatch):
    # ensure fresh import
    if 'main' in sys.modules:
        del sys.modules['main']
    return importlib.import_module('main')


def test_main_camera_not_opened(monkeypatch):
    dummy_logger = DummyLogger()
    # patch logger setup to return our dummy
    monkeypatch.setattr('src.logger_config.setup_logger', lambda *a, **k: dummy_logger)
    # patch VideoCapture to return not-opened capture
    monkeypatch.setattr('cv2.VideoCapture', lambda *a, **k: DummyCaptureNotOpened())

    # import main (should call exit / raise SystemExit)
    try:
        reload_main_with_patches(monkeypatch)
    except SystemExit:
        pass

    assert any('Não foi possível abrir a câmera' in e for e in dummy_logger.errors) or dummy_logger.errors


def test_main_no_faces_detected(monkeypatch):
    dummy_logger = DummyLogger()
    monkeypatch.setattr('src.logger_config.setup_logger', lambda *a, **k: dummy_logger)
    monkeypatch.setattr('cv2.VideoCapture', lambda *a, **k: DummyCaptureSingleFrame())
    # patch detect_faces to return empty
    monkeypatch.setattr('src.face_detector.detect_faces', lambda frame, c: tuple())
    # no-op GUI functions
    monkeypatch.setattr('cv2.imshow', lambda *a, **k: None)
    monkeypatch.setattr('cv2.waitKey', lambda *a, **k: ord('q'))
    monkeypatch.setattr('cv2.destroyAllWindows', lambda *a, **k: None)

    m = reload_main_with_patches(monkeypatch)
    # at end, logger should have info about shutdown
    assert any('Encerrado' in msg or 'Encerrado com sucesso' in msg for msg in dummy_logger.infos)


def test_main_faces_and_analysis(monkeypatch):
    dummy_logger = DummyLogger()
    monkeypatch.setattr('src.logger_config.setup_logger', lambda *a, **k: dummy_logger)
    monkeypatch.setattr('cv2.VideoCapture', lambda *a, **k: DummyCaptureSingleFrame())
    # return one face at top-left
    monkeypatch.setattr('src.face_detector.detect_faces', lambda frame, c: [(0, 0, 10, 10)])

    # mock analyze_face to return a dict-like result
    def fake_analyze(face_img):
        return {"age": 25, "gender": "Woman", "dominant_emotion": "happy"}

    monkeypatch.setattr('src.facial_analysis.analyze_face', fake_analyze)
    monkeypatch.setattr('cv2.imshow', lambda *a, **k: None)
    monkeypatch.setattr('cv2.waitKey', lambda *a, **k: ord('q'))
    monkeypatch.setattr('cv2.destroyAllWindows', lambda *a, **k: None)

    m = reload_main_with_patches(monkeypatch)
    # should have logged analysis
    assert any('Análise' in msg for msg in dummy_logger.infos) or any('Análise' in s for s in dummy_logger.infos)
