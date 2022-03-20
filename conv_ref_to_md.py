
def print_lines(lines):
    for line in lines:
        print(line, end='')

file_in = 'input.txt'
file_out = 'output.txt'

with open(file_in, 'rt') as f:
    lines = f.readlines()
# lines = lines[:50]
# print_lines(lines)
# print('')

joined_lines = []
for line in lines:
    line = line.strip()
    if line[-1] == '-':
        line = line[:-1]
    else:
        line += ' '

    if line[0] == '[':
        joined_lines.append(line)
    else:
        joined_lines[-1] += line

# print_lines(joined_lines)

md = []
for line in joined_lines:
    line = line.strip()
    line = line.replace('www. ', 'www.')
    line = line.replace('et al.', '*et al.*')
    line = line.replace('“', '"')
    line = line.replace('”', '"')
    idx1, idx2 = 0, 0
    if 'vol' in line: # journal article
        idx2 = line.find(', vol')
        if '" in' in line:
            idx1 = line.find('" in ') + 5
        elif '," ' in line:
            idx1 = line.find('," ') + 3
        else:
            idx1 = line[:idx2].rfind(', ') + 2
    elif 'in Proc' in line: # conference paper
        idx1 = line.find('in Proc') + 3
        idx2 = line[idx1:].find(',') + idx1
    if 0 < idx1 < idx2:
        line = line[:idx1] + '*' + line[idx1:idx2] + '*' + line[idx2:]
    line += '\n\n'
    md.append(line)


print_lines(md)

with open(file_out, 'wt') as f:
    f.writelines(md)

