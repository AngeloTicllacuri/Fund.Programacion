#Estructuras secuenciales

#Ejercicio 1 = Precio de libros

print("Escoga el tipo de libro")
print("(1)Lenguaje")
print("(2)Historia")
print("(3)Biologia")
print("(4)Matematicas")
tipo = int(input())
preciolenguaje = 30
preciohistoria = 40
preciobiologia = 20
preciomatematicas = 50
if tipo==1: 
	print("el precio del libro es:", preciolenguaje)
if tipo==2: 
	print("el precio del libro es:", preciohistoria)
if tipo==3: 
	print("el precio del libro es:", preciobiologia)
if tipo==4: 
	print("el precio del libro es:", preciomatematicas) 

print("(2) para pasar al siguiente ejemplo")
pasar=input()


#Ejercicio 2 = Gasto total de frutas

print("Hola casero/a que frutas desea llevar, tenemos:") 
print("manzana")
print("pera")
print("platano")
print("sandia") 
preciomanzana = 1
preciopera = 2
precioplatano = 1
preciosandia = 2
print("¿Cuantas manzanas desea?")
cant1 = int(input())
print("¿Cunatas peras desea?")
cant2 = int(input()) 
print("¡Cuantos platanos desea?")
cant3 = int(input())
print("¿Cuantas sandias desea?")
cant4 = int(input()) 
total1= preciomanzana*cant1
total2= preciopera*cant2
total3= precioplatano*cant3 
total4= preciosandia*cant4 
total5= total1+total2+total3+total4
print("Su compra sale un total de:", total5, "soles")

print("(3) para pasar al siguiente ejemplo")
pasar1=input()

#Ejercicio 3 = Bienvenida hacia una jugueria

print("Buenos dias, ¿cual es su nombre?") 
decir = input() 
print("Que tal señor",decir, ", bienvenido a nuestro local PEREZA")
comentario = input()
print("Pase por aqui porfavor, en unos momentos lo atendemos")
print("La carta:")
print("(1)especial")
print("(2)jugo de fresa")
print("(3)surtido") 
print("¿Cual desea?")
orden = input()
print("Buena elecciòn, ahora le traemos su pedido señor",decir) 

print("(4) para pasar al siguiente ejemplo")
pasar2=input()

#Ejercicio 4 = Total de ingreso de una panaderia

panchabata=2
panfrances=3
pancaracol=1

print("total de panes chabatas vendidas son:")
pre1= int(input())
print("total de panes franceses vendido son: ")
pre2= int(input()) 
print("total de panes caracoles vendidos son:")
pre3= int(input())

resultado1=panchabata*pre1 
resultado2=panfrances*pre2
resultado3=pancaracol*pre3 
rpta=resultado1+resultado2+resultado3
print("El total del dia es:", rpta,"soles") 

print("(5) para pasar al siguiente ejemplo")
pasar3=input()

#Ejercicio 5 = Cuota total de un televisor

print("Venta de productos electrodomesticos") 
print("Ingrese el nombre del producto") 
nombre=input()
print("Ingrese la cantidad de prodcutos")
cuunt=int(input())

precioproducto= 1500
cuota=precioproducto*cuunt
print("El total de su compra es:",cuota, "soles") 






