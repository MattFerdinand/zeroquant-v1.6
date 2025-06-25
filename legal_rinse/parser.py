import pathlib
from typing import Union


def read_text(path_or_string: str) -> str:
    """Read from a file path or return the string as-is."""
    p = pathlib.Path(path_or_string)
    if p.exists():
        return p.read_text()
    return path_or_string
