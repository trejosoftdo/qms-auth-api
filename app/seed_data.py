"""Entry point"""

import sys
import os

# pylint: disable=C0413
# pylint: disable=E0401

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from database.seed import run

run()
