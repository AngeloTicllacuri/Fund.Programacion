#Estructuras repetitivas (for) y acumuladores y contadores

#Ejercicio 1 = Cantidad de nummeros pares y suma de numeros impares

var=int(input("¿Cuantos nùmeros desea ingresar?:")) 
count=0 
suma= 0 
for a in range(var):
    print("Ciclo "+str(a+1)+" ") 
    lego=int(input("Ingrese un nùmero: "))
    if lego%2==0: 
        count+=1
    else: 
        suma+=lego 
print("La cantidad de numeros pares es:",count)
print("La suma de numeros impares es:",suma)

print("(2) para pasar al siguiente ejemplo") 
replit=input()  

#Ejercicio 2 =  Numeros pares

for e in range(1,21): 
    if e % 2==0: 
        print(e)


print("(3) para pasar al siguiente ejemplo") 
replit1=input() 

#Ejercicio 3 = Factorial de un numero

factor=1 
n=int(input("Digite un nùmero:"))
for o in range(1,n+1):
    factor=factor*o 
print(factor) 

print("(4) para pasar al siguiente ejemplo") 
replit2=input()

#Ejercicio 4 = Conteo de nùmeros pares

mario=0; 
for raton in range(1,5):
    luigi=int(input("Inserte un numero:")) 
    if luigi % 2==0: 
           mario=mario+1 
print("Se introdujo",mario,"nùmeros pares") 


print("(5) para pasar al siguiente ejemplo") 
replit4=input() 


#Ejercicio 5 = Introduccion de numero par o no

ind=False 
for var in range(1,3):
    capi=int(input("Dime un nùmero:"))
    if capi % 2 == 0: 
        ind=True 
if ind: 
    print("Usted introdujo un nùmero par")
else: 
    print("Usted no intrifujo un nùmero par")








