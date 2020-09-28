
tempCelsius=[-248,15, -200, -235,9, -256,0, -210,8, -259,9, -204,0]
def calcularCelsius(tempCelsius_):
    for i in range(len(tempCelsius_)):
        if tempCelsius_[i]+273.15>15:
           print(tempCelsius_[i]+273.15)
        else:
            print("No es superior")
    

print(calcularCelsius(tempCelsius))
        


