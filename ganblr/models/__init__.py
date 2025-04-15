"""Top-level package for Ganblr."""

__author__ = """Tulip Lab"""
__email__ = 'jhzhou@tuliplab.academy'
__version__ = '0.1.1'

from .kdb import KdbHighOrderFeatureEncoder
from .utils import get_demo_data

# The GANBLR models
from .models.ganblr import GANBLR
from .models.ganblrpp import GANBLRPP
from .models.ganblrmug import GANBLR_MUG

__all__ = [
    'models',
    'KdbHighOrderFeatureEncoder',
    'get_demo_data',
    'GANBLR',
    'GANBLRPP',
    'GANBLR_MUG'
]
