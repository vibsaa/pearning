csv_data=open('points.txt','r')
lines=csv_data.readlines()
csv_data.close()
#print(lines)
lines=[line.strip() for line in lines]
#print(lines)
csv_op=open('datapoints.txt','w')
csv_op.close()

for line in lines:
    data_sep=line.split(',')
    vdadc=int(data_sep[0])
    idadc=int(data_sep[1])
    #print(f" {vdadc} , {idadc} ")
    voltage=vdadc*.00654
    current=(idadc*.00654)/6.67
    #print(f"the v value is {voltage:.3f} and i value is {current:.3f} ")
    csv_val=','.join([str(voltage),str(current)])
    csv_op=open('datapoints.txt','a')
    print(csv_val)
    csv_op.write(f"{csv_val}\n")
    csv_op.close()
    