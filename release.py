import os
import zipfile

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(ROOT_DIR, "target")
PACKAGE_NAME = "leech-balancer"

INCLUDED_FILES = [
    "__init__.py",
    "main.py",
    "config.py",
    "config.json",
    "manifest.json",
]


def main():
    os.makedirs(TARGET_DIR, exist_ok=True)
    output_path = os.path.join(TARGET_DIR, PACKAGE_NAME + ".ankiaddon")

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for name in INCLUDED_FILES:
            archive.write(os.path.join(ROOT_DIR, name), name)

    print("Created %s" % output_path)


if __name__ == "__main__":
    main()
