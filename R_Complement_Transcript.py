#!/usr/bin/env python3
# shebang command executes the program with ./


def get_seq_type():  # takes the type of nucleic acid sequence
    print("what is your sequence type (d for DNA - r for RNA)")
    return input()


def get_enq_seq():
    print("type or paste your sequence?")
    return input()


def get_enq_type():  # takes the process enquired to be performed on the sequence
    print("what is your enquiry (r for reverse - c for complement - t for transcript - n for reverse complement)")
    return input()


def validate_enq_seq(value: str, sequence_type: str):
    for base in value:
        if base not in {"A", "T", "G", "C", "U", "a", "t", "g", "c", "u"}:
            print("Error: Your sequence can only include letters a, t/u, g, c only.")
            return False
        if sequence_type == "d" and base in ("U", "u"):
            print("Error: DNA strand cannot contain Uracil.")
            return False
        if sequence_type == "r" and base in ("T", "t"):
            print("Error: RNA strand cannot contain Thymine.")
            return False
    return True


def validate_enq_type(enq: str):  # validates the enquired process
    if enq not in {"r", "c", "t",
                   "n"}:  # reversed complement of a strand equals to its negative strand hence n was selected.
        print(
            "Error: Enquiry must be one of 'r' for reverse, 'c' for complement, 't' for transcript, or 'n' for reverse complement")
        return False
    else:
        print("here is your result sequence:")
        return True

def base_dictionary(base):  # defines the correct counterpart codons
    if get_seq_type() == "d" and get_enq_type() == "c":
        codon_dict = {"A": "T", "T": "A", "G": "C", "C": "G", "a": "t", "t": "a", "g": "c", "c": "g"}
        return codon_dict[base]
    else:
        codon_dict = {"A": "U", "U": "A", "G": "C", "C": "G", "a": "u", "u": "a", "g": "c", "c": "g"}
        return codon_dict[base]


def comp_trans(strand):  #returns the complement/translated sequence of the input strand
    for base in strand:
        strand += base_dictionary(base)
    return strand


def reverse_strand(strand: str):  # returns the reversed sequence of the input strand
    return strand[::-1]


def negative_strand(strand):  # returns the reversed sequence of complement/translated sequence
    return reverse_strand(comp_trans(strand))


def process_seq(strand: str, enq_type: str, seq_type: str):  # processes input strand based on the type of enquiry
    if validate_enq_seq(strand, seq_type) and validate_enq_type(enq_type):
        if enq_type == "r":
            return reverse_strand(strand)
        elif enq_type in ("c", "t"):
            return comp_trans(strand)
        elif enq_type == "n":
            return negative_strand(strand)


def main():
    sequence_type = get_seq_type()
    enquiry_type = get_enq_type()
    query = get_enq_seq()

    result = process_seq(query, enquiry_type, sequence_type)
    print(result)


if __name__ == "__main__":
    main()
