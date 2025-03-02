#! /home/maryam/miniconda3/envs/MyAwesomeApp/bin/python     #shebang command executes the program with ./

def seq_type():  # takes the type of nucleic acid sequence
    return input("what is your sequence type (d for DNA - r for RNA)")


def input_seq():  #takes the sequence
    return input("Enter your sequence: ")


def enq_type():  # takes the required process to be performed on the sequence
    print("what is your enquiry (r for reverse - c for complement - t for transcript - n for reverse complement)")
    return input()
# reversed complement of a strand equals to its negative strand hence n was selected.

codon = {"A", "T", "G", "C", "U", "a", "t", "g", "c", "u"}

if enq_type() not in ["c", "t", "r", "n"]:
    print(
        "Error: Enquiry must be one of 'r' for reverse, 'c' for complement, 't' for transcript, or 'n' for reverse complement")
else:
    def input_seq(strand):
        for base in strand:
            if base not in codon:
                return "Error: Your sequence can only include letters a, t/u, g, c only."
            if (seq_type() == "d") and ("U" or "u" in strand):
                return "Error: DNA strand cannot contain Uracil."
            if (seq_type() == "r") and ("T" or "t" in strand):
                return "Error: RNA strand cannot contain Thymine."
            else:
                def results():
                    if seq_type() == "d":
                        codon_dict = {"A": "T", "T": "A", "G": "C", "C": "G", "a": "t", "t": "a", "g": "c", "c": "g"}
                        return codon_dict[base]
                    elif seq_type() == "r":
                        codon_dict = {"A": "U", "U": "A", "G": "C", "C": "G", "a": "u", "u": "a", "g": "c", "c": "g"}
                        return codon_dict[base]


    for base in strand:
        complement += complement_codon[base]
    return complement


def reverse_string_slicing(seq_to_reverse):
    return seq_to_reverse[::-1]


def reverse_complement_dna(sequence):
    return input_seq(reverse_string_slicing(sequence))


def reversed_complement(dna_strand):
    result = reverse_complement_dna(dna_strand)
    print("your reversed cDNA strand is:", result)


seq_type = enq()
query_seq = input_seq()
reversed_complement(query_seq)
