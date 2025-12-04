"""Numpydoc test module.

.. currentmodule:: numpydoc_test_module

.. autosummary::
   :toctree: generated/

   MyClass
   my_function

Reference [1]_

References
----------
.. [1] https://numpydoc.readthedocs.io
"""

__all__ = ["MyClass", "my_function"]


class MyClass:
    """A class."""

    thisown = property(lambda x: True, lambda x, v: True, doc="The membership flag")

    def example(self, x):
        """Example method."""


def my_function(*args, **kwargs):
    """Return None."""
    return
