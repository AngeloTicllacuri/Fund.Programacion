#Estructuras repetitivas (while) y contadores y acumuladores

#Ejercicio 1 = Reales positivos


numero= int(input("Escriba un nùmero mayor a 0:")) 

while numero<0: 
    print("Error, no es un nùmero pmayor a 0") 
    numero=int(input("Vuelva a digitar un nùmero:"))

print("Cumple la condiciòn")
 
print("(2) para pasar al siguiente ejemplo") 
sema=input() 

#Ejercicio 2 = Cuenta en reversa

x = 10
while x > 0:
    x -=1
    print(x)


print("(3) para pasar al siguiente ejemplo") 
sema1=input() 

#Ejercicio 3 = Nombre forma creciente

text="Angelo" 
c=0 
while c < len(text): 
    print(text[:c+1])
    c+= 1 


print("(4) para pasar al siguiente ejemplo") 
sema2=input() 

#Ejercicio 4 = Suma consecutiva

x,y=1,2
while y < 20: 
    print(y)
    x,y= y, x*y

print("(5) para pasar al siguiente ejemplo") 
sema3=input() 

#Ejercicio 5 = Cantidad de pares e impares


n=1 
par=impar=0 
while n!=0: 
    n=int(input("Digite un numero:")) 
    if n>0: 
        if n % 2 == 0:
            par+=1 
        else: 
            impar+=1 
print("El total de numeros pares es: ", par)
print("El total de numeros impares es: ",impar)

