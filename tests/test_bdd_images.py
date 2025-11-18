"""BDD tests for images feature using pytest-bdd"""
import os
from pathlib import Path
from pytest_bdd import scenarios

# Import step definitions - must be imported before scenarios()
from tests.step_defs import common_steps
from tests.step_defs import images_steps

# Get the base directory (project root)
BASE_DIR = Path(__file__).parent.parent
FEATURE_FILE = os.path.join(BASE_DIR, 'tests', 'features', 'images.feature')

# Register all scenarios from the feature file
scenarios(FEATURE_FILE)

