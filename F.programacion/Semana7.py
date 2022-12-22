#Estructuras secuenciales y selectivas

#Ejercicio 1 =  Resolucion de preguntas

print("Responda las preguntas")
print("El valor de pi es:")
valor =int(input())
print("Hipotenusa del triangulo 35 y 45 es:")
valor1 =int(input()) 
if valor==180 and valor1==5:
    print("Saco 2/2, muy bien")
elif valor==180 and valor1!=5: 
    print("Saco 1/2, vas bien") 
elif valor!=180 and valor1==5:
    print("Saco 1/2, vas bien")
else: 
    print("Saco 0/2, ponte a estudiar") 

print("(2) para pasar al siguiente ejemplo") 
deci=input() 

#Ejercicio 2 = Almuerzo

ceviche=30
arrozconmariscos=20 

print("Escoga un plato") 
print("(1)ceviche")
print("(2)arroz con mariscos") 
escoger=int(input())
if escoger==1: 
    print("El ceviche tiene un costo de:", ceviche, "soles")
elif escoger==2: 
    print("Arroz con mariscos tiene un costo de:",arrozconmariscos,"soles")
else: 
    print("No selecciono un plato") 

print("(3) para pasar al siguiente ejemplo") 
deci1=input() 


#Ejercicio 3 = Contrato de cable

movistar=60
directv=70

print("¿Que antena desea instalar?") 
print("(1)movistar")
print("(2)directv") 
elegir=int(input())
print("¿Cuantos meses desea el servicio?") 
elegir1=int(input())

prep=elegir1*movistar 
prep1=elegir1*directv

if elegir==1:
    print("Saldria un costo de:",prep,"soles")
elif elegir==2:
    print("Podra ver su mundial a:",prep1,"soles") 
else: 
    print("Cambiate a claro") 


print("(4) para pasar al siguiente ejemplo") 
deci2=input() 

#Ejercicio 4 = Promedio de amonestaciones

print("¿Cuantas amonestaciones tuviste en el primer partido?")
var=int(input())
print("¿Cuantas en el segundo partido?") 
var1=int(input())
print("¿Cuantas en el tercer partido?") 
var2=int(input())

resultado=(var+var1+var2)/3 
if resultado<5: 
    print("Proda jugar el siguiente partido")
else: 
    print("Se perdera el siguiente partido") 


print("(5) para pasar al siguiente ejemplo") 
deci3=input() 

#Ejercicio 5 = perdida de frutas

print("En la mesa habia 10 manzanas y 8 peras") 
print("¿Cuantas manzanas te comiste?") 
frut=int(input())
print("¿Cuantas peras te comiste?")
frut1=int(input()) 

resta=(18-frut-frut1)

if resta<=4: 
    print("Estas catigado")
else: 
    print("Te la paso por esta vez")











