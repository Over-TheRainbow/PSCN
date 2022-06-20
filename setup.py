import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PSCN-Over-TheRainbow",
    version="0.0.13",
    author="Over-TheRainbow",
    author_email="chan.2019@alumni.ubc.ca",
    description="A small PSCN package, most of the code is from tvayer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Over-TheRainbow/PSCN",
    project_urls={
        "Bug Tracker": "https://github.com/Over-TheRainbow/PSCN/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)