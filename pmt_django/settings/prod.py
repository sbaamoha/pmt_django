"""Production settings"""

import os
from .common import *

DEBUG = int(os.environ.get("DEBUG", 0)) == 1
