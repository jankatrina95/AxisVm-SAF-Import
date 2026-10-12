"""Import von SAF-Dateien nach AxisVM."""

from .saf_reader import SafModel, read_saf

__all__ = ["SafModel", "read_saf"]
__version__ = "0.1.0"
