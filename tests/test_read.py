import sys

from read_toml import read_toml

if sys.version_info >= (3, 4):
    import pathlib
else:
    import pathlib2 as pathlib


def test_read(
    tmp_path,  # type: pathlib.Path
):
    # type: (...) -> None
    f = tmp_path / "pyproject.toml"
    f.write_bytes(b"")
    assert read_toml(str(f)) == {}
