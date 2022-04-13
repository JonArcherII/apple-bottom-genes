import json
import glob
import os
import sys

from compare import *

if len(sys.argv) <= 1 or len(sys.argv) > 2:
    print('Improper usage')
    exit()

try:
    dna = open(sys.argv[1], 'r')
except Exception:
    print("Fatal Error: Unable to open DNA file '" + sys.argv[1] + "'.")
    exit(1)

for filename in glob.glob('markers/*.json'):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        j = json.load(f)
        lines = dna.readlines()
        for line in lines:
            dictionary = check_string(line, j)
            if dictionary is None:
                continue
            names = ""
            for name in dictionary['names']:
                names += name + ", "
            names = names.strip(" ,")
            print("Match for Gene \"" +
                  names + "\" with RSID " + dictionary['rsid'])
            print("\tChromosome: ", dictionary['chromosome'])
            print("\tPosition: ", dictionary['position'])
            print("\tAlleles: " +
                  dictionary['allele1'] + ", " + dictionary['allele2'])
            print("\tAssociation: " + j['association'])
            print(
                "\tNote: This is NOT a diagnosis! If you want to be diagnosed/screened, please consult your doctor.")
            print(
                "\tMore resources here (no affiliation): https://www.ncbi.nlm.nih.gov/snp/" + dictionary['rsid'] + '\n')
