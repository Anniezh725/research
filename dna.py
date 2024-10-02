def read_dna(dna_file):
    dna_pairs = []
    with open(dna_file, 'r') as file:
        for line in file:
            pair = line.strip().split('<->')
            pair = tuple(base.strip() if base.strip() else '' for base in pair)
            dna_pairs.append(pair)
    return dna_pairs
    """
    Read a DNA string from a file.
    the file contains data in the following format:
    A <-> T
    G <-> C
    G <-> C
    C <-> G
    G <-> C
    T <-> A
    Output a list of touples:
    [
        ('A', 'T'),
        ('G', 'C'),
        ('G', 'C'),
        ('C', 'G'),
        ('G', 'C'),
        ('T', 'A'),
    ]
    Where either (or both) elements in the string might be missing:
    <-> T
    G <->
    G <-> C
    <->
    <-> C
    T <-> A
    Output:
    [
        ('', 'T'),
        ('G', ''),
        ('G', 'C'),
        ('', ''),
        ('', 'C'),
        ('T', 'A'),
    ]
    """
    pass

def is_rna(dna):
    dna_bases = {'A', 'T', 'G', 'C'}
    rna_bases = {'A', 'U', 'G', 'C'}
    dna_count = sum(base[0] in dna_bases and base[1] in dna_bases for base in dna if '' not in base)
    rna_count = sum(base[0] in rna_bases and base[1] in rna_bases for base in dna if '' not in base)
    total_bases = len([base for base in dna if '' not in base])
    if total_bases == 0:
        return "Invalid"
    dna_percentage = dna_count / total_bases
    rna_percentage = rna_count / total_bases
    if dna_percentage >= 0.9:
        return "DNA"
    elif rna_percentage >= 0.9:
        return "RNA"
    else:
        return "Invalid"
    """
    Given DNA in the aforementioned format,
    return the string "DNA" if the data is DNA,
    return the string "RNA" if the data is RNA,
    return the string "Invalid" if the data is neither DNA nor RNA.
    DNA consists of the following bases:
    Adenine  ('A'),
    Thymine  ('T'),
    Guanine  ('G'),
    Cytosine ('C'),
    RNA consists of the following bases:
    Adenine  ('A'),
    Uracil   ('U'),
    Guanine  ('G'),
    Cytosine ('C'),
    The data is DNA if at least 90% of the bases are one of the DNA bases.
    The data is RNA if at least 90% of the bases are one of the RNA bases.
    The data is invalid if more than 10% of the bases are not one of the DNA or RNA bases.
    Empty bases should be ignored.
    """
    pass


def clean_dna(dna):

    cleaned_dna = []
    for pair in dna:
        base1, base2 = pair
        if base1 == '' and base2 == '':
            continue  # Ignore pairs with both bases empty
        elif base1 == '':
            base1 = {'T': 'A', 'A': 'T', 'C': 'G', 'G': 'C', 'U': 'A'}[base2]
        elif base2 == '':
            base2 = {'T': 'A', 'A': 'T', 'C': 'G', 'G': 'C', 'U': 'A'}[base1]
        elif base1 == 'T' or base1 == 'U':
            if base2 != 'A':
                continue  # Invalid pair, skip
        elif base1 == 'A':
            if base2 != 'T' and base2 != 'U':
                continue  # Invalid pair, skip
        elif base1 == 'G':
            if base2 != 'C':
                continue  # Invalid pair, skip
        elif base1 == 'C':
            if base2 != 'G':
                continue  # Invalid pair, skip
        cleaned_dna.append((base1, base2))
    return cleaned_dna
    """
    Given DNA in the aforementioned format,
    If the pair is incomplete, ('A', '') or ('', 'G'), ect
    Fill in the missing base with the match base.
    In DNA 'A' matches with 'T', 'G' matches with 'C'
    In RNA 'A' matches with 'U', 'G' matches with 'C'
    If a pair contains an invalid base the pair should be removed.
    Pairs of empty bases should be ignored.
    """
    pass

def mast_common_base(dna):
    bases_count = {}
    for base1, _ in dna:
        if base1 != '':
            bases_count[base1] = bases_count.get(base1, 0) + 1
    if bases_count:
        return max(bases_count, key=bases_count.get)
    else:
        return None
    """
    Given DNA in the aforementioned format,
    return the most common first base:
    eg. given:
    A <-> T
    G <-> C
    G <-> C
    C <-> G
    G <-> C
    T <-> A
    The most common first base is 'G'.
    Empty bases should be ignored.
    """
    pass

def base_to_name(base):
    base_names = {'A': 'Adenine', 'T': 'Thymine', 'G': 'Guanine', 'C': 'Cytosine', 'U': 'Uracil'}
    return base_names.get(base, 'Unknown')


    """
    Given a base, return the name of the base.
    The base names are:
    Adenine  ('A'),
    Thymine  ('T'),
    Guanine  ('G'),
    Cytosine ('C'),
    Uracil   ('U'),
    return the string "Unknown" if the base isn't one of the above.
    """
    pass
