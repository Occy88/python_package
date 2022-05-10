try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="python_package_template",
    version="0.0.0",
    author="",
    author_email="Add the email here",
    description="Add a description here.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seclea/python_package_template",
    packages=find_packages(exclude=["test"]),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
)
