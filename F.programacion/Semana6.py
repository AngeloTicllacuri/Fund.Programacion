#Estructuras selectivas

#Ejercicio 1 = Nùmero mayor

num1=float(input("Ingrese el primer nùmero:"))
num2=float(input("Ingrese el segundo nùmero:"))
num3=float(input("Ingrese el tercer nùmero:")) 

if num1>num2 and num1>num3:
    print(num1, "es mayor") 
elif num2>num3 and num2>num1:
    print(num2, "es mayor")
else: 
    print(num3, "es mayor") 

print("(2) para pasar al siguiente ejemplo") 
dec=input() 

#Ejercicio 2 = valor de pi

pi=180 

trigo=float(input("ingrese el valor de pi:"))

if trigo==pi: 
    print("es correcto")
else: 
    print("es incorrecto") 

print("(3) para pasar al siguiente ejemplo") 
dec1=input() 

#Ejercicio 3 = Nùmeros reales

number=float(input("Ingrese un nùmero:")) 

if number>0:
    print("El nùmero es un  real positivo")
elif number==0: 
    print("El nùmero es cero")
else:
    print("El nùmero es un real negativo") 

print("(4) para pasar al siguiente ejemplo") 
dec2=input() 

#Ejercicio 4 = par o impar 

count= int(input("Coloque un nùmero:")) 
count1=int(input("Coloque otro nùmero"))

if count%2==0 and count1%2==0: 
    print("Ambos nùmeros son pares") 
elif count%2==0 and count1%2!=0: 
    print(count,"es par") 
elif count%2!=0 and count1%2==0: 
    print(count1,"es par") 
else: 
    print("Ambos son nùmeros impares") 


print("(5) para pasar al siguiente ejemplo") 
dec3=input()  

#Ejercicio 5 = Compra de productos

fucion= int(input("Digite precio del movil:"))
fucion1= int(input("Digite precio de airpods::")) 

total=fucion+fucion1 
if total<900: 
    print("Alcanza el dinero")
else:
    print("No alcanza el dinero")










