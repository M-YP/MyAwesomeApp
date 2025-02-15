def complement_dna(dna_strand):
    base_code = {"A", "T", "G", "C", "a", "t", "g", "c"}
    for codon in dna_strand:
        if codon not in base_code:
            return "Error: Input must include letters a,t,g,c only."

    complement = ""
    complement_codon = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
        "a": "t",
        "t": "a",
        "c": "g",
        "g": "c",
    }

    for codon in dna_strand:
        complement += complement_codon[codon]
    return complement


def reverse_string_slicing(cdna_to_reverse):
    return cdna_to_reverse[::-1]


def reverse_complement_dna(rcdna):
    return complement_dna(reverse_string_slicing(rcdna))


def print_rcdna(rcdna):
    result = reverse_complement_dna(rcdna)
    print("your reversed cDNA strand is:", result)


def input_strand():
    return input("Enter your DNA strand: ")


query_dna = input_strand()
print_rcdna(query_dna)
