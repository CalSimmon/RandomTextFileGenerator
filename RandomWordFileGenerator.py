from random_word import RandomWords
import random
import sys
import argparse
import os

class TextFileGenerator():
    def __init__(self, number_of_files, file_length, word_list):
        self.random_generator = RandomWords()
        self.number_of_files = int(number_of_files)
        self.file_length = int(file_length)
        self.word_list = word_list
        self.current_random_words = None
        self.output_folder()

    def get_random_words_list(self):
        self.current_random_words = self.random_generator.get_random_words()
        while self.current_random_words == None:
            self.current_random_words = self.random_generator.get_random_words()

    def generate_file(self, name):
        self.get_random_words_list()
        with open(name, 'w') as f:
            for i in range(self.file_length):
                currentLine = ''
                for x in range(random.randrange(15, 30, 1)):
                    if ((random.randrange(1, 5, 1)) == 1) and not (self.word_list == None):
                        currentLine += f'{random.choice(self.word_list)} '
                    else: 
                        currentLine += f'{random.choice(self.current_random_words)} '
                f.write(f'{currentLine}\n')

    def generator(self):
        for n in range(self.number_of_files):
            name = f'Output/testing_file{n}.txt'
            self.generate_file(name)

    def output_folder(self):
        if not os.path.isdir('Output'):
            os.mkdir('Output')

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generates N number of files with L number of lines using random full words.  Can include a word list if you need specific words included at random.")
    parser.add_argument('Number of files', metavar='N', type=int, help="Number of files to create")
    parser.add_argument('Number of lines', metavar='L', type=int, help="Number of lines to add to each file")
    parser.add_argument('-w', '--word-list', metavar='[TEXT]', nargs='*', help="Word list should you want specific words included")

    args = parser.parse_args()
    return args

def main():
    args = vars(parse_arguments())
    generator = TextFileGenerator(args['Number of files'], args['Number of lines'], args['word_list'])
    generator.generator()

if __name__ == '__main__':
    main()