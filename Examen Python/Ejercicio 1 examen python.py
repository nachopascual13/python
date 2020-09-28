
radios=[5.3,6.8,9.0,10,3.4]
from math import pi

def calcularperimetro(radios_):
    for i in range(len(radios_)):
        print(2*3.14*radios_[i])

print(calcularperimetro(radios))
    
