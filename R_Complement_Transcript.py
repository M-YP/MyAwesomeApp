def enq():
    return input("what is your sequence type (d for DNA - r for RNA)")

def input_seq(strand):
    return input("Enter your sequence: ")

def enquiry_type():
    return input(
        "what is your enquiry (c for complement - t for transcript - r for reverse - n for reverse complement)")
# reversed complement of a strand equals to its negative strand hence n was selected.

def results():
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
    if enquiry_type() in ["c", "n", "t"]:
        def complement_seq(strand):
            base_code = {"A", "T", "G", "C", "U", "a", "t", "g", "c", "u"}
            for single_base in strand:
                if single_base not in base_code:
                    return "Error: Input must include letters a, t/u, g, c only."
                if (enq() == "d") and ("U" or "u" in strand):
                    return "Error: DNA strand cannot contain U/u."
                if (enq() == "r") and ("T" or "t" in strand):
                    return "Error: RNA strand cannot contain T/t."


    if input == "r":
        complement_codon["U"] = "A"
        complement_codon["u"] = "a"
        complement_codon["A"] = "U"
        complement_codon["a"] = "u"

    for base in strand:
        complement += complement_codon[base]
    return complement


def reverse_string_slicing(seq_to_reverse):
    return seq_to_reverse[::-1]


def reverse_complement_dna(sequence):
    return complement_seq(reverse_string_slicing(sequence))


def reversed_complement(dna_strand):
    result = reverse_complement_dna(dna_strand)
    print("your reversed cDNA strand is:", result)


seq_type = enq()
query_seq = input_seq()
reversed_complement(query_seq)
