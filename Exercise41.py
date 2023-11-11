a=str(input('Ten not nhac: '))
b=int(input('Nhap so quang tam: '))
C4=261.63
D4= 293.66
E4= 329.63 
F4= 349.23 
G4= 392.00 
A4=  440.00 
B4= 493.88
if a=='C':
    tanso=C4 / 2**(4-b)
elif a=='D':
    tanso=D4 / 2**(4-b)
elif a=='E':
    tanso=E4 / 2**(4-b)
elif a=='F':
    tanso=F4 / 2**(4-b)
elif a=='G':
    tanso=G4 / 2**(4-b)
elif a=='A':
    tanso=A4 / 2**(4-b)
elif a=='B':
    tanso=B4 / 2**(4-b)
print('Tan so cua ',a,b, ' la:', round(tanso,2),'Hz', sep="")