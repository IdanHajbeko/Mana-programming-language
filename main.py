from functions import *

while True:
    while True:
        file_name = input("Enter file name: ")
        if not file_name.endswith(".mana"):
            print("File name must end with .mana")
        else:
            break
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    else:
        break

for i, line in enumerate(lines):
    try:
        parse_line(line.strip())
    except Exception as e:
        print(f"Error in line {i+1}: {e}")
