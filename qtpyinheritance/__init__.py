from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from . import properties
from . import signals

__all__ = ['properties', 'signals']
