def validate_strand(strand: str, is_rna: bool) -> (bool, str):
    base_code = {"A", "T", "G", "C", "U", "a", "t", "g", "c", "u"}
    for codon in strand:
        if codon not in base_code:
            return False, "Error: Input must include letters a, t/u, g, c only."
        if not is_rna and codon in {"U", "u"}:
            return False, "Error: DNA strand cannot contain U/u."
        if is_rna and codon in {"T", "t"}:
            return False, "Error: RNA strand cannot contain T/t."

    return True, None


def complement_seq(strand: str, is_dna: bool) -> str:
    complement = ""
    complement_codon = {
        "A": "T" if is_dna else "U",
        "T": "A",
        "C": "G",
        "G": "C",
        "a": "t" if is_dna else "u",
        "t": "a",
        "c": "g",
        "g": "c",
        "u": "a" if is_dna else "?",
        "U": "A" if is_dna else "?",
    }
    if is_dna:
        complement_codon.pop("u")
        complement_codon.pop("U")

    for codon in strand:
        complement += complement_codon[codon]

    return complement


def reverse_string_slicing(cseq_to_reverse: str) -> str:
    return cseq_to_reverse[::-1]


def reverse_complement_dna(rcseq: str, kind: str) -> str:
    return complement_seq(reverse_string_slicing(rcseq), kind in {"d", "D"})


def print_rcdna(rc_seq: str, kind: str = "d"):
    result = reverse_complement_dna(rc_seq, kind)
    print("your reversed cDNA strand is:", result)


def get_seq_kind():
    return input("what is your sequence type (d for DNA - r for RNA)").strip()


def input_seq():
    return input("Enter your sequence: ").strip()


def get_inputs() -> (str, str):
    seq_type = get_seq_kind()
    is_valid = seq_type in ["d", "r", "R", "D"]
    if not is_valid:
        print("Error: your sequence must be D: DNA or R: RNA.")
        return None, None
    query_seq = input_seq()
    is_valid, error_message = validate_strand(query_seq, seq_type in ["R", "r"])
    if not is_valid:
        print(error_message)
        return None, None
    return query_seq, seq_type


if __name__ == "__main__":
    query, kind = get_inputs()
    if not query or not kind:
        exit(1)

    print_rcdna(query, kind)
