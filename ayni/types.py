"""This module is concerned with defining any custom types for ayni.
"""

from enum import Enum


class Extension(Enum):
    """Extension is an Enum class representing the file extensions that
    ayni supports.
    """

    python = ".py"
