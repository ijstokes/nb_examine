"""
Utility for ensuring that each javascript file is loaded exactly once for a Jupyter
python interpreter.
"""

from __future__ import print_function

import os
from IPython.display import display, Javascript
import time

my_dir = os.path.dirname(__file__)

LOADED_JAVASCRIPT = set()

def load_if_not_loaded(filenames, verbose=False, delay=0.1, force=False):
    """
    Load a javascript file to the Jupyter notebook context,
    unless it was already loaded.
    """
    loaded = False
    for filename in filenames:
        if not os.path.exists(filename):
            filename = os.path.join(my_dir, filename)
        assert os.path.exists(filename), "no such file " + repr(filename)
        if force or not filename in LOADED_JAVASCRIPT:
            if verbose:
                print("loading javascript file", filename)
            display(Javascript(filename))
            LOADED_JAVASCRIPT.add(filename)
            loaded = True
        else:
            if verbose:
                print ("not reloading javascript file", filename)
        if loaded and delay > 0:
            if verbose:
                print ("delaying to allow JS interpreter to sync.")
            time.sleep(delay)
