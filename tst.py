import sys
if sys.prefix != sys.base_prefix:
    print("running")
else:
    print("Not running")

