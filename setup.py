#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="moof",
    version="0.1.0",
    summary="a simple terminal program that allows to move a dot with arrow keys and leave colored traces",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "moof = moof.main:main"
        ]
    },
)
