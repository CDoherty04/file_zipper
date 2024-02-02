import zipfile
import pathlib


def make_archive(filepaths, destination):
    # Adds slashes and compressed.zip to the end of the created file's name
    destination_path = pathlib.Path(destination, "compressed.zip")
    with zipfile.ZipFile(destination_path, "w") as archive:
        for filepath in filepaths:
            # Create path object to eliminate absolute path problem when zipped
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


# Test
if __name__ == "__main__":
    make_archive(["a.txt", "b.txt"], "dest")
