import sys
import re

args = sys.argv[1:]

if not args:
    print("none")
else:
    for work in args:
        if not re.search(r'ism$', work):
            print(f"{work}ism")