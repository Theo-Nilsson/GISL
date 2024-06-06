import sys
import os

# Add parent directory to Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Import the GISL class
from src.gisl import GISL

# Instantiate GISL object
gisl = GISL()

# Test get_address() function

# Test with valid coordinates
lat, lng = 52.5200, 13.4050  # Berlin, Germany
print(gisl.get_address(lat, lng))  # Expected output: Address of Berlin, Germany

# Test with invalid coordinates
lat, lng = 200, 200  # Invalid coordinates
print(gisl.get_address(lat, lng))  # Expected output: Could not determine the address for (200, 200).

# Test with ocean coordinates (no address)
lat, lng = 0, 0  # Coordinates in the ocean
print(gisl.get_address(lat, lng))  # Expected output: Could not determine the address for (0, 0).

# Test get_public_ip() function

# Test with a system having a valid public IP address
print(gisl.get_public_ip())  # Expected output: Public IP address of the system

# Test with a system having no internet connection
# Note: Simulating no internet connection is tricky in automated tests.
