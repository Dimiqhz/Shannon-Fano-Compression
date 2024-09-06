# Shannon-Fano Compression

This repository contains a Python implementation of the **Shannon-Fano Coding Algorithm**, a method for lossless data compression. Shannon-Fano coding is based on assigning binary codes to symbols in proportion to their probabilities, ensuring efficient compression.

## How Shannon-Fano Coding Works

Shannon-Fano coding is a method of variable-length, prefix-free encoding that assigns shorter binary codes to more frequent characters and longer codes to less frequent characters. It is similar to Huffman coding but differs in how the binary tree is constructed.

## Shannon-Fano Coding Overview

Shannon-Fano coding is a lossless data compression algorithm, which assigns variable-length prefix-free binary codes to characters based on their probabilities. The most frequent characters are assigned shorter codes, and the least frequent ones are assigned longer codes. The key steps involve sorting the symbols by their probabilities and recursively splitting them into two parts with approximately equal total probabilities.

This method ensures that no code is a prefix of another code, allowing for unambiguous decoding of the compressed data.

## Files Generated

- `compressed_text.txt`: Contains the compressed binary data.
- `dict.txt`: Contains the dictionary of characters and their corresponding Shannon-Fano codes.

### Steps:
1. **Frequency Calculation**: The frequency of each character in the text is calculated.
2. **Probability Assignment**: The relative frequency (probability) of each character is calculated.
3. **Sorting by Probability**: Characters are sorted by decreasing probability.
4. **Splitting the List**: The list of characters is split into two parts, such that the total probabilities of each part are as equal as possible.
5. **Assigning Codes**: Each character in the left part is assigned a binary `0`, and each in the right part is assigned a binary `1`. The process is recursively repeated for each part.
6. **Compression**: The input text is compressed by replacing characters with their assigned binary codes.

## Features

- Compresses text using the Shannon-Fano coding algorithm.
- Accepts input from the user or from a file.
- Outputs the compressed text to `compressed_text.txt`.
- Generates a dictionary of characters and their corresponding Shannon-Fano codes in `dict.txt`.

## Functions

### `compress_data(data)`
- **Purpose**: Compresses the input text using Shannon-Fano coding.
- **Process**:
    - Calculates the probability (relative frequency) of each character in the input data.
    - Uses the `splitter` function to split the sorted list of characters.
    - Recursively encodes the characters by assigning binary codes using the `encoder` function.
    - Saves the compressed text to `compressed_text.txt` and the dictionary to `dict.txt`.

### `splitter(probability, pointer)`
- **Purpose**: Splits the sorted list of character probabilities into two parts with approximately equal total probabilities.
- **Process**:
    - Recursively compares the total probability of the left and right parts, adjusting the split point to minimize the difference between the two.

### `encoder(compressor, split)`
- **Purpose**: Assigns binary codes to each character based on the Shannon-Fano method.
- **Process**:
    - The left part of the split is assigned a `0`, and the right part is assigned a `1`. The process is repeated recursively for each part until all characters have binary codes.

### `main()`
- **Purpose**: Handles user input and manages text input.
- **Process**:
    - Prompts the user to either input text manually or load it from a file.
    - Calls the `compress_data` function to compress the input text.
    - Outputs the compressed text and dictionary to files.

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/Dimiqhz/Shannon-Fano-Compression.git
    ```
2. Run the Python script:
    ```bash
    python shannon_fano_compress.py
    ```
3. Follow the prompts to either enter text manually or specify a file for compression.
