lista=["R1",'R2','R3','S1','S2','S3','R4','R5','PC']
for i in lista:
    if 'S' in i:
        print(i,end=' ')
    elif "R" in i:
        print(i,end=' ')
    else:
        print(i,"No es un equipo de red")