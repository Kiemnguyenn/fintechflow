import pathlib

def show_banner():

    root_dir = pathlib.Path(__file__).resolve().parent.parent.parent
    banner_path = root_dir / "resources" / "banner.txt"

    try:
        with open(banner_path, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        pass