# constants.py
# Purpose: define paths used for dashboard
# Single responsibility, this files handle paths

# Base path
# Path(__file__) = absolute path to this file (constants.py)
# .parents[0]   = utils/          (one level up)
# .parents[1]   = ATP_2025/dashboard/    BASE_PATH (two levels up)

from pathlib import Path

BASE_PATH = Path(__file__).parents[1]

STYLING_PATH = BASE_PATH / "styling"

CONTENT_PATH = BASE_PATH / "content"
