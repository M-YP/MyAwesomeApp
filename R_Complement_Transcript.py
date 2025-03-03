#!/usr/bin/env python3
# shebang command executes the program with ./

def seq_type():  # takes the type of nucleic acid sequence
    return input("what is your sequence type (d for DNA - r for RNA)")


def input_seq():  #takes the sequence
    return input("Enter your sequence: ")


def enq_type():  #takes the required process to be performed on the sequence
    print("what is your enquiry (r for reverse - c for complement - t for transcript - n for reverse complement)")
    return input()
# reversed complement of a strand equals to its negative strand hence n was selected.

codon = {"A", "T", "G", "C", "U", "a", "t", "g", "c", "u"}  #shows the eligible codons in the input sequence

if enq_type() not in ["c", "t", "r", "n"]:  #validates the enquired process
    print(
        "Error: Enquiry must be one of 'r' for reverse, 'c' for complement, 't' for transcript, or 'n' for reverse complement")


def seq_validation(strand):  # validates the input sequence for the eligible codons in DNA and/or RNA
    for base in strand:
        if base not in codon:
            return "Error: Your sequence can only include letters a, t/u, g, c only."
        if (seq_type() == "d") and ("U" or "u" in strand):
            return "Error: DNA strand cannot contain Uracil."
        if (seq_type() == "r") and ("T" or "t" in strand):
            return "Error: RNA strand cannot contain Thymine."


def base_dictionary(base):  # defines the correct counterpart codons
    if seq_type() == "d" and enq_type() == "c":
        codon_dict = {"A": "T", "T": "A", "G": "C", "C": "G", "a": "t", "t": "a", "g": "c", "c": "g"}
        return codon_dict[base]
    else:
        codon_dict = {"A": "U", "U": "A", "G": "C", "C": "G", "a": "u", "u": "a", "g": "c", "c": "g"}
        return codon_dict[base]


def comp_trans(strand):  #returns the complement/translated sequence of the input strand
    for base in strand:
        strand += base_dictionary(base)
    return strand


def reverse_strand(strand):  # returns the reversed sequence of the input strand
    return strand[::-1]


def negative_strand(strand):  # returns the reversed sequence of complement/translated sequence
    return reverse_strand(comp_trans(strand))


def process_seq(strand):  # processes input strand based on the type of enquiry
    if seq_validation(strand) is None:
        if enq_type() == "r":
            return reverse_strand(strand)
        elif enq_type() == "c":
            return comp_trans(strand)
        elif enq_type() == "t":
            return comp_trans(strand)
        elif enq_type() == "n":
            return negative_strand(strand)
