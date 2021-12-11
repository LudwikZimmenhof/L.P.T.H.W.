import math
dl=int(input("Podaj długość: "))
c=(input("Który bok: dłuższa przyprostokątna (a), krótsza przyprostokątna (b), przeciwprostokątna (c): "))
def find(x):
    global przypkr
    global przec
    global przypdl
    if c=="c":
        przec=x
        przypkr=x/2
        przypdl=przypkr*math.sqrt(3)
    elif c=="b":
        przypkr=x
        przypdl=x*math.sqrt(3)
        przec=x*2
    elif c=="a":
        przypdl=x
        przypkr=x/math.sqrt(3)
        przec=przypkr*2
    print(f'przeciwprostokątna: {przec}, krótsza przyprostokątna: {przypkr}, dłuższa przyprostokątna: {przypdl} √{przypdl*przypdl}')
find(dl)

def obw():
    print(f'Obwód równa się: {przec + przypkr + przypdl} lub {przec + przypkr} + √{przypdl*przypdl}')
obw()
