from os import path
import sys

from setuptools import find_packages, setup

from obp.version import __version__

here = path.abspath(path.dirname(__file__))
sys.path.insert(0, path.join(here, "obp"))

print("version")
print(__version__)

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

package_data_list = ["obp/policy/conf/prior_bts.yaml", "obp/dataset/obd"]

setup(
    name="obp",
    version=__version__,
    description="Open Bandit Pipeline: a python library for bandit algorithms and off-policy evaluation",
    url="https://github.com/st-tech/zr-obp",
    author="Yuta Saito",
    author_email="open-bandit-project@googlegroups.com",
    keywords=["bandit algorithms", "off-policy evaluation"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "matplotlib>=3.8.0",
        "mypy-extensions>=0.4.3",
        "numpy>=1.25.0",
        "pandas>=2.1.0",
        "pyyaml>=6.0.1",
        "seaborn>=0.12.2",
        "scikit-learn>=1.6.1",
        "scipy>=1.15.2",
        "torch>=2.6.0",
        "tqdm>=4.65.0",
        "pyieoe>=0.1.1",
        "pingouin>=0.4.0",
    ],
    license="Apache License",
    packages=find_packages(
        exclude=["benchmark", "docs", "examples", "obd", "tests", "slides"]
    ),
    package_data={"obp": package_data_list},
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
    ],
)
