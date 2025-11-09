"""BDD tests for users feature using pytest-bdd"""
import os
from pathlib import Path
from pytest_bdd import scenario

# Import step definitions
from tests.step_defs import common_steps, users_steps

# Get the base directory (project root)
BASE_DIR = Path(__file__).parent.parent

# Import scenarios from feature files
scenario(os.path.join(BASE_DIR, 'tests', 'features', 'users.feature'), 'Display users with no records')
scenario(os.path.join(BASE_DIR, 'tests', 'features', 'users.feature'), 'Display users with status colors')

