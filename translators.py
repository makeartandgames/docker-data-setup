import distances 
import json 

codon_table = {
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',    # Serine
    'TTC': 'F', 'TTT': 'F',    # Phenylalanine
    'TTA': 'L', 'TTG': 'L',    # Leucine
    'TAC': 'Y', 'TAT': 'Y',    # Tirosine
    'TAA': '*', 'TAG': '*',    # Stop
    'TGC': 'C', 'TGT': 'C',    # Cisteine
    'TGA': '*',    # Stop
    'TGG': 'W',    # Tryptofan
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',    # Leucine
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',    # Proline
    'CAC': 'H', 'CAT': 'H',    # Histidine
    'CAA': 'Q', 'CAG': 'Q',    # Glutamine
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',    # Arginine
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I',    # Isoleucine
    'ATG': 'M',    # Methionine
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',    # Threonine
    'AAC': 'N', 'AAT': 'N',    # Asparagine
    'AAA': 'K', 'AAG': 'K',    # Lysine
    'AGC': 'S', 'AGT': 'S',    # Serine
    'AGA': 'R', 'AGG': 'R',    # Arginine
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',    # Valine
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',    # Alanine
    'GAC': 'D', 'GAT': 'D',    # Aspartic Acid
    'GAA': 'E', 'GAG': 'E',    # Glutamic Acid
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G'     # Glycine
}

sequences = {
  "X": "CTGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG",
  "Y": "ATGGCCATTGTAATGGGCCGCTGAAGGGGTGCCCGATAC"
}

ERROR_CHAR = '?'
def translate_dna(dna, codon_table):
    skip_range = [i for i in range(0, len(dna) - 2, 3)]
    return ''.join(codon_table.get(dna[i:i+3], ERROR_CHAR) for i in skip_range)

def load_json(filename):
    with open(filename) as f:
        return json.load(f)

def unused_function():

    codon_table = load_json("codon_table.json")
    sequences = load_json("sequences.json")

def hamming_protein_comparison(X, Y, codon_table):
    protein_X = translate_dna(X, codon_table)
    protein_Y = translate_dna(Y, codon_table)
    protein_distance = distances.hamming_distance(protein_X, protein_Y)
    return X, Y, protein_distance

def compare_default_sequences():
    
    X = sequences["X"]
    Y = sequences["Y"]
    return compare_sequences(X, Y, codon_table)

def compare_sequences(X, Y, codon_table):
    dna_distance = distances.hamming_distance(X, Y)
    return X, Y, dna_distance 



