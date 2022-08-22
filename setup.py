from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in djangoproject/__init__.py
from djangoproject import __version__ as version

setup(
	name="djangoproject",
	version=version,
	description="ERPNext Laboratory Utility is an Frappe App for facilitating Laboratory",
	author="epics",
	author_email="aadithp210@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
