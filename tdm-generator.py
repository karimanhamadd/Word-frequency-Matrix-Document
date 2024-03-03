#!/usr/bin/env python3
import os
import sys
#import sys

def read_directory(input_dir):

	return sorted(os.listdir(input_dir))

def read_term_freq(file_path):

	term_freq = {}
	with open(file_path, 'r') as file:
		for line in file:
			term, frequency = line.strip().split()
			#we NEED to covert from string to integer to be able to store 
			#it in the dictionary 
			term_freq[term] = int(frequency)
	return term_freq

def create_matrix(sorted_files, sorted_terms, input_dir):

	matrix = [[0] * len(sorted_files) for _ in range(len(sorted_terms))]
	
	term_to_index = {term: i for i, term in enumerate(sorted_terms)}
	file_to_index = {file: i for i, file in enumerate(sorted_files)}

	for i, filename in enumerate(sorted_files):
		term_freq = read_term_freq(os.path.join(input_dir, filename))
		for term in term_freq:
			matrix[term_to_index[term]][i] = term_freq[term]

	return matrix

def save_output(output_dir, sorted_files, sorted_terms, matrix):
	with open(os.path.join(output_dir, 'sorted_documents.txt'), 'w') as file:
		for filename in sorted_files:
			file.write(filename + '\n')
	with open(os.path.join(output_dir, 'sorted_terms.txt'), 'w') as file:
		for term in sorted_terms:
			file.write(term + '\n')

	with open(os.path.join(output_dir, 'td_matrix.txt'), 'w') as file:
		file.write(f"{len(sorted_terms)} {len(sorted_files)}\n")
		for row in matrix:
			file.write(' '.join(map(str, row)) + '\n')

def main():


	if len(sys.argv) != 3:
		sys.exit(1)

	input_dir = sys.argv[1]
	output_dir = sys.argv[2]
	

	os.makedirs(output_dir, exist_ok=True) 

	sorted_files = read_directory(input_dir)
	terms = set()
	for filename in sorted_files:
		terms.update(read_term_freq(os.path.join(input_dir, filename)))
	sorted_terms = sorted(terms)
	matrix = create_matrix(sorted_files, sorted_terms, input_dir)
	save_output(output_dir, sorted_files, sorted_terms, matrix)

if __name__ == "__main__":
    main()




