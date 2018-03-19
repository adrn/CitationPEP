# Standard library
import importlib
import sys

__all__ = ['citation']


def citation(package=None):
    if package is None:
        packages = sys.modules.keys()

    else:
        packages = [package]

    citations = dict()
    for package in packages:
        if isinstance(package, str):
            package = importlib.import_module(package)

        try:
            citations[package.__name__] = package.__citation__
        except AttributeError:
            continue

    return citations
