import argparse
from src.cli import main as app_main


def parse_args():
    p = argparse.ArgumentParser(description="Run FaceMatch Info CLI")
    p.add_argument("--camera", type=int, default=0, help="Camera index for cv2.VideoCapture")
    p.add_argument("--no-gui", dest="show_gui", action="store_false", help="Disable GUI display (useful for headless runs)")
    p.add_argument("--log-file", dest="log_file", default=None, help="Optional log file path")
    return p.parse_args()


def main():
    args = parse_args()
    app_main(camera_index=args.camera, show_gui=args.show_gui, log_filename=args.log_file)


if __name__ == "__main__":
    main()
