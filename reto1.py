#Recibir un numero en teclado y determinar si este es múltiplo de 5
print('Bienvenido a mi reto 1 en python')

numero=int(input('Digite un numero: '))
 
resultado= numero%3

print(f'El modulo del numero digitado es: {resultado}')

#CREANDO UN CONDICIONAL
if(resultado==0):
    print("es multiplo de 3")
else:
    print("No es multipo de 3")