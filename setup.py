from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in clinic_app/__init__.py
from clinic_app import __version__ as version

setup(
	name="clinic_app",
	version=version,
	description="An Appointment Booking App",
	author="Montego-arch",
	author_email="arch@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
