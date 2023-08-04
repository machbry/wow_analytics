from setuptools import setup

setup(
    name="wlogs",
    version="0.1",
    package_dir={"wlogs": "wlogs"},
    packages=["wlogs"],
    package_data={'wlogs': ['containers/*.py']}
)
