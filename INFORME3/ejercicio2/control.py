"""Servirá para mostrar las opciones de conversion
   y realizar el control del programa"""

print(
      """En el siguiente programa usted encontrará unas opciones de conversión,
         partiendo de: 

            * un decimal
            * un octal
            * un binario
            * un hexadecimal
         
         que podrán ser cambiados entre ellos. usted deberá seleccionar la base
         según a continuación.

            * decimal : 1
            * binario : 2
            * octal : 3
            * hexadecimal : 4
         
         y despues tendrá que digitar el numero, tenga en cuenta que debe ser
         entero, despues podrá escoger a cual cambiar.
      """)

x= input("ingrese la base del numero: ")
n= input("ingrese el numero a convertir: ")
if x== "1":
   import Decimal 
   print("""este modulo tiene 3 metodos:
            
            * conversionABinaria
            * conversionAOctal
            * conversionAHexadecimal  
            
            que se escogen segun la lista siguiente
            
            * binario : 1
            * octal : 2
            * hexadecimal : 3
            """)
   y=input("ingrese la base a convertir: ")

   if y== "1": print("la conversion es: ", Decimal.convertirABinario(n))
   if y== "2": print("la conversion es: ", Decimal.convertirAOctal(n))
   if y== "3": print("la conversion es: ", Decimal.convertirAHexadecimal(n))
if x== "2":
   import binario 
   print("""este modulo tiene 3 metodos:
            
            * conversionADecimal
            * conversionAOctal
            * conversionAHexadecimal  
            
            que se escogen segun la lista siguiente
            
            * decimal : 1
            * octal : 2
            * hexadecimal : 3
            """)
   y=input("ingrese la base a convertir: ")

   if y== "1": print("la conversion es: ", binario.convertirADecimal(n))
   if y== "2": print("la conversion es: ", binario.convertirAOctal(n))
   if y== "3": print("la conversion es: ", binario.convertirAHexadecimal(n))
if x== "3":
   import octal
   print("""este modulo tiene 3 metodos:
            
            * conversionADecimal
            * conversionABinario
            * conversionAHexadecimal  
            
            que se escogen segun la lista siguiente
            
            * decimal : 1
            * binario : 2
            * hexadecimal : 3
            """)
   y=input("ingrese la base a convertir: ")

   if y== "1": print("la conversion es: ", octal.convertirADecimal(n))
   if y== "2": print("la conversion es: ", octal.convertirABinario(n))
   if y== "3": print("la conversion es: ", octal.convertirAHexadecimal(n))
if x== "4":
   import hexadecimal
   print("""este modulo tiene 3 metodos:
            
            * conversionADecimal
            * conversionABinario
            * conversionAOctal 
            
            que se escogen segun la lista siguiente
            
            * decimal : 1
            * binario : 2
            * octal : 3
            """)
   y=input("ingrese la base a convertir: ")

   if y== "1": print("la conversion es: ", hexadecimal.convertirADecimal(n))
   if y== "2": print("la conversion es: ", hexadecimal.convertirABinario(n))
   if y== "3": print("la conversion es: ", hexadecimal.convertirAOctal(n))