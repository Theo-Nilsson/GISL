import sys
import os

# Add parent directory to Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.gisl import GISL

gisl = GISL()

# Test with valid coordinates
lat, lng = 52.5200, 13.4050  # Berlin, Germany
print(gisl.get_timezone(lat, lng))  # Expected output: Europe/Berlin

# Test with invalid coordinates
lat, lng = 179, 179  # Invalid coordinates
print(gisl.get_timezone(lat, lng))  # Expected output: Could not determine the time zone for (9999, 9999).

# Test with ocean coordinates (no timezone)
lat, lng = 0, 0  # Coordinates in the ocean
print(gisl.get_timezone(lat, lng))  # Expected output: Could not determine the time zone for (0, 0).
