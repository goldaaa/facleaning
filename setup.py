#!/usr/bin/env python
# coding=utf-8

from setuptools import setup
import io

with io.open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="facleaning",
    description="Improved display of Farsi text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='0.1.0',
    platforms="ALL",
    license="MIT",
    packages=['facleaning'],
    install_requires=[],
    author="navid nasiri",
    author_email="goldaaa.program@gmail.com",
    maintainer="navid nasiri",
    maintainer_email="goldaaa.program@gmail.com",
    package_dir={'facleaning': 'facleaning'},
    test_suite='facleaning.test',
    include_package_data=True,
    keywords="facleaning persian farsi iran",
    url="https://github.com/goldaaa/facleaning",
    download_url="https://github.com/goldaaa/facleaning/tarball/master",
    package_data={},
    setup_requires=[],
    python_requires=">=3.5",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: Persian',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        'Topic :: Software Development :: User Interfaces',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],  # https://test.pypi.org/pypi?%3Aaction=list_classifiers
)
