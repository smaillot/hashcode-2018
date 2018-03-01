import argparse
from os import path, makedirs

try:
    from tqdm import tqdm as progress
except:
    print("Please install tqdm for loading bar display")
    def progress(range):
        return range

def parsing():

    parser = argparse.ArgumentParser(description='hashcode template program') 
    parser.add_argument('input', help='name of input file in inputs directory', type=str)
    parser.add_argument('-n', help='number of tries', type=int, default=100)
    parser.add_argument('-p', help='number of CPUs', type=int, default=2)

    return parser.parse_args()

def write_list(f, list):

    f.write(" ".join([str(n) for n in list]) + "\n")

def write_array(f, array):

    for line in array:        
        
        write_list(f, line)

def read_line(reader):

    return [int(i) for i in reader.readline().split(" ")]

def read_array(reader, n_lines):

    return [read_line(reader) for _ in range(n_lines)]

def read_input(input_file):
    
    with open('inputs/' + input_file + '.in', 'r') as reader:
        ## init params
        input1, = read_line(reader)
        
        ## read array 
        array = read_array(reader, input1)    
    
    return input1, array

def write_output(input, name, score, output):

    if not path.exists('outputs'):

        makedirs('outputs')

    with open('outputs/' + input + '_' + name + '_' + str(score) + '.out', 'w') as f:

        write_list(f, [len(output)])
        write_array(f, output)

def display(solution, loaded_input):

    print(solution)

def print_score(score, loaded_input, time):

    print("score \t{} found in\t{:.6}s".format(score, time))