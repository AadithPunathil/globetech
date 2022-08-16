from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in globetech/__init__.py
from globetech import __version__ as version

setup(
	name="globetech",
	version=version,
	description="globetech",
	author="aadith.p@indictrans.in",
	author_email="aadith.p@indictrans.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
