"""BDD tests for products feature using pytest-bdd"""
import os
from pathlib import Path
from pytest_bdd import scenario

# Import step definitions
from tests.step_defs import common_steps, products_steps

# Get the base directory (project root)
BASE_DIR = Path(__file__).parent.parent

# Import scenarios from feature files
scenario(os.path.join(BASE_DIR, 'tests', 'features', 'products.feature'), 'Display products with stock color indicators')
scenario(os.path.join(BASE_DIR, 'tests', 'features', 'products.feature'), 'Display loading indicator during API delay')

