"""Tornar o pacote instalavel."""
from setuptools import setup, find_packages

setup(
    name="desafio_storm",
    version="0.1.0",
    description="API que resolve os desafios propostos",
    include_package_data=True,
    install_requires=["flask", "flask-restful"],
)
