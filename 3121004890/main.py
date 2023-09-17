import sys

def read_file(file_path):
    with open(file_path,'r') as file:
        return file.read()

if __name__=='__main__':
    original_file = sys.argv[1]
    file_to_check=sys.argv[2]
    output_file=sys.argv[3]