from setuptools import setup, find_packages

setup(
    name="o-pyIP",
    version="0.1",
    packages=find_packages(),
    package_data={'': ['banner.txt']},
    install_requires=[
        "netifaces",
        "tabulate",
        "argparse",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "pi = src.cli:main",
        ]
    },
)
