# Future
from __future__ import annotations

# Standard Library
import re

# Packages
import setuptools


with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()

with open("requirements.txt") as file:
    INSTALL_REQUIRES = file.read().splitlines()

with open("slate/__init__.py") as file:
    VERSION = re.search(r"^__version__: [^=]* = \"([^\"]*)\"", file.read(), re.MULTILINE).group(1)

CLASSIFIERS = [
    "Framework :: AsyncIO",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: Implementation :: CPython",
    "Operating System :: OS Independent",
    "Environment :: Other Environment",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "Typing :: Typed"
]

PROJECT_URLS = {
    "Documentation": "https://slate.readthedocs.io/en/latest/",
    "Issue Tracker": "https://github.com/Axelancerr/slate/issues",
    "Source":        "https://github.com/Axelancerr/slate",
}

EXTRAS_REQUIRE = {
    "docs": [
        "sphinx",
        "sphinxcontrib_trio",
        "faculty-sphinx-theme",
    ],
}

setuptools.setup(
    author="Axelancerr",
    classifiers=CLASSIFIERS,
    description='A lavalink, andesite and obsidian websocket/api wrapper.',
    extras_require=EXTRAS_REQUIRE,
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    license="MIT",
    name="slate",
    packages=["slate", "slate.objects", "slate.obsidian", "slate.obsidian.objects", "slate.typings"],
    project_urls=PROJECT_URLS,
    python_requires=">=3.9.0",
    url="https://github.com/Axelancerr/slate",
    version=VERSION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
)
