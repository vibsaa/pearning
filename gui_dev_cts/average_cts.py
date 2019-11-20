from numpy import genfromtxt

files = ["datapoints.txt", "points.txt"]

data = genfromtxt(files[0], delimiter=',')
for f in files[1:]:
    data += genfromtxt(f, delimiter=',')

data /= len(files)
#print(data[220])
file=open("data123.txt",'w')
file.writelines(str(data))
file.close()

csv_data=open('data123.txt','r')
lines=csv_data.readlines()
csv_data.close()
#print(lines)
lines=[line.strip() for line in lines]
#print(lines)
for line in lines:
    data_sep=line.split(' ')
    vdadc=int(data_sep[0])
    idadc=int(data_sep[1])
    print(f" {vdadc} , {idadc} ")
