import tkinter as tk
from tkinter import simpledialog

output = []
file_path = 'input.txt'

# Function to return the complement base of a given DNA base
def complement_base(base):
    if base == 'A':
        return 'T'
    elif base == 'T':
        return 'A'
    elif base == 'C':
        return 'G'
    elif base == 'G':
        return 'C'
    else:
        return ''

# Function to return the complement sequence of a given DNA sequence
def complement_sequence(sequence):
    complement = ''
    for base in sequence:
        complement += complement_base(base)
    return complement

# Function to find complementary pairs of DNA sequences
def find_complementary_pairs(file_path, sequence_length):
    sequences = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extract non-empty sequences from the input file
    for line in lines:
        line = line.strip()
        if line:
            sequences.append(line)

    num_sequences = len(sequences)
    for i in range(num_sequences):
        for j in range(i+1, num_sequences):
            original_sequence = sequences[i]
            sequence_to_exam = sequences[j]

            sub_sequence_len = len(sequence_to_exam)
            sub_sequences = []

            # Generate all possible subsequences of the given length from the sequence
            for k in range(sub_sequence_len - sequence_length + 1):
                sub_sequences.append(sequence_to_exam[k : k + sequence_length])

            # Check if the complement of any subsequence is present in the original sequence
            for s in range(len(sub_sequences)):
                complement = complement_sequence(sub_sequences[s])
                if original_sequence.__contains__(complement):
                    start_index = original_sequence.find(complement_sequence(sub_sequences[s]))
                    # Add a message to the output list specifying the complementary pairs
                    output.append(f'A sequence on line [{i+1}] --{original_sequence}-- starting from letter number [{start_index+1}] has inside a complementary of --{sub_sequences[s]}-- that is on line [{j+1}] starting from letter number [{s+1}].')

# Function to write the output list to a file
def write_output():
    file_path = "output.txt"

    with open(file_path, 'w') as file:
        for line in range(len(output)):
            file.write(output[line])
            file.write("\n")
    # File writing is complete
    print("Writing to file is done.")

def main():
    root = tk.Tk()
    root.withdraw()

    # Prompt the user to enter the length of the sequence
    number = simpledialog.askinteger("Enter the length of the sequence", "Please, enter the length of the sequence you wish to find and also notice\nthat the file with all sequences to search in has to be named 'input.txt'.")

    if number is not None:
        # Find complementary pairs based on user input
        find_complementary_pairs(file_path, number)
        # Write the output to a file
        write_output()
    else:
        print("Dialog canceled.")
        root.destroy()

main()