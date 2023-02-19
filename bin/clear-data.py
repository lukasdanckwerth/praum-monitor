import os
from pathlib import Path


def is_dir(path):
    return Path(path).is_dir()


def is_file(path):
    return Path(path).is_file()


def clear_dir(path):
    files = Path(path).glob('*')

    if len(list(files)) == 0:
        print("already empty")
        exit(0)

    for f in files:
        try:
            if is_dir(f):
                clear_dir(f.absolute().as_posix())
                os.rmdir(f.absolute().as_posix())
                print("Removed directory: " + f.absolute().as_posix())
            elif is_file(f):
                f.unlink()
                print("Removed file: " + f.absolute().as_posix())
            else:
                print("Invalid file: " + f.absolute().as_posix())

        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))


clear_dir("data")
