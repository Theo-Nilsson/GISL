# GISL (Geographic Information System Library)

GISL is a Python library that provides functionality for various Geographic Information System (GIS) tasks such as retrieving country names, continents, latitude and longitude information, addresses, timezones, and public IP addresses.

## Features

- Retrieve country names and continents based on country codes.
- Obtain latitude and longitude information from IP addresses. \
<strong style="color: #FF5500; font-size: 0.75rem; font-weight: bolder;">Latitude and longitude from IP address is not allways fully reliable</strong>
- Calculate distances between coordinates.
- Determine timezones based on coordinates.
- Reverse geocoding to get address information from coordinates.
- Get the public IP address of the current machine.

## Installation

You can install GISL via pip:
```bash
pip install gisl
```

## Usage
Here's a basic example of how to use GISL:
```python
from gisl import GISL

gisl = GISL()

country_name = gisl.get_country("US")
print("Country Name:", country_name)
```

Output:
```
Country Name: United States
```