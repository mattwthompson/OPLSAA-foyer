from setuptools import setup

setup(
    name="oplsaafoyer",
    version="0.0",
    description="OPLS-AA plugin for foyer",
    url="http://github.com/mattwthompson/oplsaafoyer",
    author="Matthew W. Thompson",
    author_email="matt.thompson@vanderbilt.edu",
    license="MIT",
    entry_points={
        "foyer.external_forcefields": [
            "get_ff_path = oplsaafoyer.oplsaafoyer:get_ff_path"]
    },
    packages=["oplsaafoyer"],
    zip_safe=False,
)
