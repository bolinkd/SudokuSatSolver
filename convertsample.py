new_file = ""
for line in open('sample.txt', 'r'):
    for char in line:
        if char.isdigit() and char != '0' or char == '\n':
            new_file += char
        else:
            new_file += '*'
    new_file += '\n'
open('sample.txt', 'w').write(new_file)
            