import os

#read file
def read_file(filename1):
    lines = []
    with open(filename1, 'r', encoding = 'utf-8-sig') as f: #utf-8 is common encode type.
        for line in f:
            lines.append(line.strip()) #remove '\n'
    return lines


#convert
def convert(lines):
    new = []
    person = None
    for line in lines:
        if "Allen" in line:
            person = 'Allen:'        
            continue
        if "Tom" in line:
            person = 'Tom:'
            continue
        if person:
            new.append(person + ' ' + line)

    return new


#write file
def write_file(filename, lines):
    with open(filename, 'w', encoding = 'utf-8') as f:
        for line in lines:
            f.write(line + '\n')

def main(filename):
    if os.path.isfile(filename): #check the file is exist or not
        lines = read_file(filename)
        lines = convert(lines)
        write_file('output.txt', lines)
    else:
        print("Can't not find input file!")

main('input.txt')
