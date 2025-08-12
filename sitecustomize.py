import sys
import os
import importlib.util

# Custom location for .pyc files
CUSTOM_PYC_DIR = os.path.abspath("C:/Vialume/Sanctum/.cache/compiled")

def custom_cache_from_source(path, debug_override=None):
    filename = os.path.basename(path)
    name, _ = os.path.splitext(filename)
    pyc_filename = f"{name}.cpython-{sys.version_info.major}{sys.version_info.minor}.pyc"
    return os.path.join(CUSTOM_PYC_DIR, pyc_filename)

importlib.util.cache_from_source = custom_cache_from_source

