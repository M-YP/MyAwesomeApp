def seq_type():
    return input("what is your sequence type (d for DNA - r for RNA)")


def input_seq(strand):
    return input("Enter your sequence: ")


def enquiry_type():
    return input(
        "what is your enquiry (c for complement - t for transcript - r for reverse - n for reverse complement)"
    )


# reversed complement of a strand equals to its negative strand hence n was selected.
if enquiry_type() == "n" or "t" or "n":
    complement_transcript = ""
    codon_dict: dict[str, str] = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
        "a": "t",
        "t": "a",
        "c": "g",
        "g": "c",
    }


def complement_seq(strand):
    base_code = {"A", "T", "G", "C", "U", "a", "t", "g", "c", "u"}
    for codon in strand:
        if codon not in base_code:
            return "Error: Input must include letters a, t/u, g, c only."
        if (seq_type() == "d") and ("U" or "u" in strand):
            return "Error: DNA strand cannot contain U/u."
        if (seq_type() == "r") and ("T" or "t" in strand):
            return "Error: RNA strand cannot contain T/t."

    if input == "r":
        complement_codon["U"] = "A"
        complement_codon["u"] = "a"
        complement_codon["A"] = "U"
        complement_codon["a"] = "u"

    for codon in strand:
        complement += complement_codon[codon]
    return complement


def reverse_string_slicing(seq_to_reverse):
    return seq_to_reverse[::-1]


def reverse_complement_dna(sequence):
    return complement_seq(reverse_string_slicing(sequence))


def reversed_complement(dna_strand):
    result = reverse_complement_dna(dna_strand)
    print("your reversed cDNA strand is:", result)


seq_type = seq_type()
query_seq = input_seq()
reversed_complement(query_seq)
