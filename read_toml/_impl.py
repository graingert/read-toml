import io
import sys

if False:
    from typing import Any

    from _typeshed import AnyPath as StrOrBytesPath
    from _typeshed import SupportsRead

__all__ = ["TOMLDecodeError", "read_toml"]


if sys.version_info < (3, 6):
    from toml import load as _toml_load_str

    def _toml_load_bytes(
        f,  # type: SupportsRead[bytes]
    ):
        # type: (...) -> dict[str, Any]
        w = io.TextIOWrapper(f, encoding="utf8", newline="")
        try:
            return _toml_load_str(w)
        finally:
            w.detach()

    from toml import TomlDecodeError as TOMLDecodeError
else:
    from tomli import TOMLDecodeError
    from tomli import load as _toml_load_bytes


def read_toml(
    path,  # type: StrOrBytesPath | int
):
    # type: (...) -> dict[str, Any]
    with io.open(path, "rb") as f:
        return _toml_load_bytes(f)
