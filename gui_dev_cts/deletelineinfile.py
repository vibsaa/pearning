import fileinput
phrase='DONE'
for line in fileinput.input('points.txt', inplace=True):
    if phrase in line:
        continue
    print(line, end='')