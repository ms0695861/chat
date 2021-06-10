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
        new.append([person, line])
    return new


#write file
def write_file(filename2, new):
    with open(filename2, 'w', encoding = 'utf-8') as f:
        for n in new:
            f.write(n[0] + n[1] + '\n')

def main(filename1, filename2):
    if os.path.isfile(filename1) and os.path.isfile(filename2): #check the file is exist or not
        lines = read_file(filename1)
        new = convert(lines)
        write_file(filename2, new)
    else:
        print("Can't not find file")

filename1 = 'input.txt'
filename2 = 'output.txt'

main('input.txt', 'output.txt')

