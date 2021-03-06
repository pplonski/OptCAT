"""Awesome package."""

import logging

from pkg_resources import DistributionNotFound
from pkg_resources import get_distribution

from . import core

try:
    distribution = get_distribution(__name__)
    __version__ = distribution.version
except DistributionNotFound:
    pass

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()

logger.addHandler(handler)

logger.setLevel(logging.INFO)
