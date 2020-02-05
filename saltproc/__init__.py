# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
SaltProc is the first open-source tool for liquid-fueled Molten Salt Reactors
depletion simulation.
"""
from __future__ import absolute_import, division, print_function
from .version import __version__  # noqa
from .materialflow import *
from .depcode import *
from .simulation import *
from .process import *
from .reactor import *
