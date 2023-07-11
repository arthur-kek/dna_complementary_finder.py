# DNA Complementary Sequence Finder

This Python script allows you to find complementary pairs of DNA sequences within an input file. It provides a user-friendly dialog window using the `tkinter` library to input the desired length of the sequence to find.

## Prerequisites

- Python 3.x
- `tkinter` library (usually comes pre-installed with Python)

## Usage

1. Ensure that the DNA sequences to search are stored in a file named `input.txt`, with each sequence on a separate line.

2. Run the script by executing the `main()` function.

3. A dialog window will appear, asking you to enter the length of the sequence you wish to find. Provide the length and click "OK".

4. The script will search for complementary pairs of sequences and generate an output file named `output.txt` with the results.

## Example

Suppose we have an `input.txt` file with the following content:

GAGC
TTCG
CGAT
AGCTCGATCGATCGATCGA
GCTAAGCTAAGCTAAGCTA
AGCTAGCTAGCTAGCTAGCTA

If we run the script and enter a sequence length of 4, the `output.txt` file will contain the following output:

A sequence on line [1] --GAGC-- starting from letter number [1] has inside a complementary of --CTCG-- that is on line [4] starting from letter number [3].
A sequence on line [2] --TTCG-- starting from letter number [1] has inside a complementary of --AAGC-- that is on line [5] starting from letter number [4].
A sequence on line [2] --TTCG-- starting from letter number [1] has inside a complementary of --AAGC-- that is on line [5] starting from letter number [9].
A sequence on line [2] --TTCG-- starting from letter number [1] has inside a complementary of --AAGC-- that is on line [5] starting from letter number [14].
A sequence on line [3] --CGAT-- starting from letter number [1] has inside a complementary of --GCTA-- that is on line [5] starting from letter number [1].
A sequence on line [3] --CGAT-- starting from letter number [1] has inside a complementary of --GCTA-- that is on line [5] starting from letter number [6].
A sequence on line [3] --CGAT-- starting from letter number [1] has inside a complementary of --GCTA-- that is on line [5] starting from letter number [11].
A sequence on line [3] --CGAT-- starting from letter number [1] has inside a complementary of --GCTA-- that is on line [5] starting from letter number [16].
A sequence on line [3] --CGAT-- starting from letter number [1] has inside a complementary of --GCTA-- that is on line [6] starting from letter number [2].
A sequence on line [3] --CGAT-- starting from letter number [1] has inside a complementary of --GCTA-- that is on line [6] starting from letter number [6].
A sequence on line [3] --CGAT-- starting from letter number [1] has inside a complementary of --GCTA-- that is on line [6] starting from letter number [10].
A sequence on line [3] --CGAT-- starting from letter number [1] has inside a complementary of --GCTA-- that is on line [6] starting from letter number [14].
A sequence on line [3] --CGAT-- starting from letter number [1] has inside a complementary of --GCTA-- that is on line [6] starting from letter number [18].
A sequence on line [4] --AGCTCGATCGATCGATCGA-- starting from letter number [5] has inside a complementary of --GCTA-- that is on line [5] starting from letter number [1].
A sequence on line [4] --AGCTCGATCGATCGATCGA-- starting from letter number [4] has inside a complementary of --AGCT-- that is on line [5] starting from letter number [5].
A sequence on line [4] --AGCTCGATCGATCGATCGA-- starting from letter number [5] has inside a complementary of --GCTA-- that is on line [5] starting from letter number [6].
A sequence on line [4] --AGCTCGATCGATCGATCGA-- starting from letter number [4] has inside a complementary of --AGCT-- that is on line [5] starting from letter number [10].
A sequence on line [4] --AGCTCGATCGATCGATCGA-- starting from letter number [5] has inside a complementary of --GCTA-- that is on line [5] starting from letter number [11].
A sequence on line [4] --AGCTCGATCGATCGATCGA-- starting from letter number [4] has inside a complementary of --AGCT-- that is on line [5] starting from letter number [15].
A sequence on line [4] --AGCTCGATCGATCGATCGA-- starting from letter number [5] has inside a complementary of --GCTA-- that is on line [5] starting from letter number [16].
A sequence on line [4] --AGCTCGATCGATCGATCGA-- starting from letter number [4] has inside a complementary of --AGCT-- that is on line [6] starting from letter number [1].
A sequence on line [4] --AGCTCGATCGATCGATCGA-- starting from letter number [5] has inside a complementary of --GCTA-- that is on line [6] starting from letter number [2].
A sequence on line [4] --AGCTCGATCGATCGATCGA-- starting from letter number [6] has inside a complementary of --CTAG-- that is on line [6] starting from letter number [3].
... ... ...

## License

This project is licensed under the [MIT License](LICENSE).

