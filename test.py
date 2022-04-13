import json
import glob
import os
import sys

from compare import *

if len(sys.argv) <= 1 or len(sys.argv) > 2:
    print('Improper usage')
    exit()

try:
    file = open(sys.argv[1], 'r')
except Exception:
    print("Fatal Error: Unable to open DNA file '" + sys.argv[1] + "'.")
    exit(1)

test = json.load(file)

matches = 0
for filename in glob.glob('markers/*.json'):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        j = json.load(f)
        lines = test['psuedofile']
        for line in lines:
            dictionary = check_string(line, j)
            if dictionary is None:
                continue
            if dictionary['rsid'] == test['expected']['rsids'][matches]:
                matches += 1

if matches == test['expected']['number']:
    print("Passed!")
else:
    print("Failed!")
