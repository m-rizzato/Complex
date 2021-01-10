from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name="Complex",
    version="1.0",
    description="Implementation of the complex number class",
    author="Matteo RIZZATO",
    author_email="mrizzato@advestis.com",
    packages=find_packages(),
    python_requires=">=3.7",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    install_requires=install_requires,
)
