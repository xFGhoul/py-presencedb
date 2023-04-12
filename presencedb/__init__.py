from typing import Tuple

from .abc import *
from .activity import *
from .client import Client
from .enums import ActivityID
from .errors import *
from .user import *
from .utils import humanize_duration, icon_to_bytes

__all__: Tuple[str, ...] = (
    "Client",
    "ActivityID",
    "icon_to_bytes",
    "humanize_duration",
)

__version__ = "2.0.0"
__author__ = "Ghoul"
__license__ = "MIT"
