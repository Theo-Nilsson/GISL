from setuptools import setup, find_packages
from src.gisl_libinfo import Libinfo
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "readme.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = "\n" + f.read()

VERSION = Libinfo.get_version()
DESCRIPTION = Libinfo.get_description()

setup(
    name=Libinfo.get_name(),
    version=VERSION,
    author=Libinfo.get_author(),
    author_email=Libinfo.get_author_email(),
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["geopy", "geocoder", "pycountry", "pycountry_convert", "requests", "timezonefinder"],
    keywords=["python", "geography", "geocoding", "timezone", "timezones", "location"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
