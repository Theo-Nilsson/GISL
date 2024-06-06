import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from src.gisl import GISL

gisl = GISL()

# Latitude and Longitude

# Valid IP address
print(gisl.get_lat_lng("2a02:aa1:114d:8ec1:e816:8993:dc45:597e"))

# Invalid IP address
print(gisl.get_lat_lng("2a02:aa1:114d:8ec1:e816:86h3:3c4p:ea9e::::"))

# Non-existent IP address
print(gisl.get_lat_lng("2a02:aa1:114d:8ec1:e816:86h3:3c4p:ea9e"))

# Difference between coordinates

# Valid latitude and longitude
print(gisl.get_distance_between_coords((41.49008, -71.312796), (41.499498, -81.695391), km=True))

# Invalid latitude and longitude
print(gisl.get_distance_between_coords((41.49008, "string"), (41.499498, "-81.695391"), km=True))
