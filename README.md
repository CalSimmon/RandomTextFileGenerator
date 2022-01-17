# RandomWordFileGenerator.py

A generator that creates N number of files with L number of lines using random words to create long files for testing purposes.  Can include a custom word list if sepcific words are required.

## 1. Setup:
`pip install -r requirements.txt`

## 2. Parameters:
    N - Number of text files to create, INT
    L - Number of lines to add per file, INT
    -w, --word-list - Optional, list of words that should be included, [[TEXT] [TEXT] ...]

## 3. Example:
`python3 RandomWordFileGenerator.py 10 100 -w word1 word2 word3`