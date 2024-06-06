import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from src.gisl import GISL

gisl = GISL()

# Get country by code

# Valid country code
print(gisl.get_country("SE"))

# Invalid country code
print(gisl.get_country("DEE"))

# Non-existent country code
print(gisl.get_country("XX"))

# Get code by country

# Valid country name
print(gisl.get_country_code("Sweden"))

# Invalid country name
print(gisl.get_country_code("s"))

# Non-existent
print(gisl.get_country_code("Invalidistan"))