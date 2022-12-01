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
   import moduloDecimal 
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

   if y== "1": print("la conversion es: ", moduloDecimal.convertirABinario(n))
   if y== "2": print("la conversion es: ", moduloDecimal.convertirAOctal(n))
   if y== "3": print("la conversion es: ", moduloDecimal.convertirAHexadecimal(n))
if x== "2":
   import moduloBinario 
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

   if y== "1": print("la conversion es: ", moduloBinario.convertirADecimal(n))
   if y== "2": print("la conversion es: ", moduloBinario.convertirAOctal(n))
   if y== "3": print("la conversion es: ", moduloBinario.convertirAHexadecimal(n))
if x== "3":
   import moduloOctal
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

   if y== "1": print("la conversion es: ", moduloOctal.convertirADecimal(n))
   if y== "2": print("la conversion es: ", moduloOctal.convertirABinario(n))
   if y== "3": print("la conversion es: ", moduloOctal.convertirAHexadecimal(n))
if x== "4":
   import moduloHexadecimal
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

   if y== "1": print("la conversion es: ", moduloHexadecimal.convertirADecimal(n))
   if y== "2": print("la conversion es: ", moduloHexadecimal.convertirABinario(n))
   if y== "3": print("la conversion es: ", moduloHexadecimal.convertirAOctal(n))