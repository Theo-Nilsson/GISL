import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from src.gisl import GISL

gisl = GISL()

# Valid country code
print(gisl.get_continent("DE"))

# Invalid country code
print(gisl.get_continent("DEEEE"))

# Non-existent country code
print(gisl.get_continent("XX"))