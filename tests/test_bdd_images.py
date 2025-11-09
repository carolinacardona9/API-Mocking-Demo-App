"""BDD tests for images feature using pytest-bdd"""
import os
from pathlib import Path
from pytest_bdd import scenario

# Import step definitions
from tests.step_defs import common_steps, images_steps

# Get the base directory (project root)
BASE_DIR = Path(__file__).parent.parent

# Import scenarios from feature files
scenario(os.path.join(BASE_DIR, 'tests', 'features', 'images.feature'), 'Load images successfully')
scenario(os.path.join(BASE_DIR, 'tests', 'features', 'images.feature'), 'Abort image loading to speed up tests')
scenario(os.path.join(BASE_DIR, 'tests', 'features', 'images.feature'), 'Abort partial image set')

