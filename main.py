from src.parser import parsing
import sys


if len(sys.argv) == 2:
    config_file =sys.argv[1]

    
else:
    print("python3 main.py [config_file]")

file_parse = parsing.Read_input_file()
print(f"{file_parse.read_file(config_file)}")