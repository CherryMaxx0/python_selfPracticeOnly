import sys
import pandas as pd
import numpy as np

if sys.prefix != sys.base_prefix:
    print("running")
else:
    print("Not running")
print(f"Pandas version: {pd.__version__}")
print(f"Numpy version: {np.__version__}")

