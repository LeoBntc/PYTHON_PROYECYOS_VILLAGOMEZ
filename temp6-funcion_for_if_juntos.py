listasw=[]
listart=[]
listaotros=[]
lista=["R1",'R2','R3','S1','S2','S3','R4','R5','PC','Ps5','Ps4','PsP']
for i in lista:
    if 'S' in i:
       listasw.append(i)
    elif 'R' in i:
        listart.append(i)
    else:
        listaotros.append(i)
print('Switches:',listasw,'\nRouters:',listart,'\nDispositivos:',listaotros)