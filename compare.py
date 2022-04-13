def is_match(rsid, position, chromosome, allele1, allele2, spec):
    # Make sure RSID matches
    if rsid != spec['rsid']:
        return False
    # Make sure we are in the correct chromosome
    if chromosome != spec['chromosome']:
        return False
    # Compare against all associated allele pairs
    for pair in spec['alleles']:
        # Account for allele reversal (i.e. A,T and T,A should be treated the same)
        if (allele1 == pair['allele1'] and allele2 == pair['allele2']) or (allele1 == pair['allele2'] and allele2 == pair['allele1']):
            # Yay! We have a match! Oh, wait...
            return True
    return False


def check_string(string, speclist):
    for gene in speclist['genes']:
        # Break line into components
        components = string.replace('\t', ' ').strip().split()
        if len(components) != 5:
            break

        # If either of these fail, skip silently as we're likely just on a comment line
        try:
            chromosome = int(components[1].strip())
            position = int(components[2].strip())
        except Exception as e:
            break

        rsid = components[0].strip()
        allele1 = components[3].strip()
        allele2 = components[4].strip()
        if is_match(rsid, position, chromosome, allele1, allele2, gene):
            return {"rsid": rsid, "names": gene['names'], "chromosome": chromosome, "position": position,
                    "allele1": allele1, "allele2": allele2, "association": speclist['association']}
    return
