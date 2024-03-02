# convert_of_time_to_word
Programa para convertir una hora a texto.

A continuación, se detallará la estructura y las funciones del código.

El usuario deberá ingresar una hora y se le retornará el equivalente en texto. Por ejemplo: si el usuario ingresa "5:10", el programa retornará "ten minutes past five".

# Variables:
  Lista de palabras a usar times[]:
  Esta lista contiene 5 palabras predeterminadas para usarse en las frases, son: "O' clock", "past", "quarter", "half", "to".

  Diccionario de los números en inglés numbers{}: 
  El diccionario contiene los números del 1 al 29, pero no incluye el 15, 30 y 45.

  minute: El valor es el minuto ingresado y determina cómo se construirá la frase final, ya que se usa mayormente en las decisiones de los if en la función principal del programa.

  hour: Contiene la hora y se utiliza más para decidir si se imprimirá unas frases muy específicas.

  El valor que obtienen estas últimas dos variables (minute y hour) se utiliza para acceder al diccionario (numbers{}) para poder extraer su conversión a texto de los números, y para acceder a las palabras de la lista (times[]) vienen definidos los valores de acuerdo a los if de la función election().

El código está estructurado por 5 funciones, sin contar la función de __init__():
  - def verify_time():
    Esta función se encarga de comprobar que el usuario ingrese correctamente una hora para que se convierta a texto.

  - def election():
    Es la principal función donde se pasarán los parámetros de hora (hour) y minuto (minute). Se constituye por varios if donde cada uno corroborará cómo se va a imprimir la frase final, primero se verifica si se inserta una hora en específica para imprimir esa hora que ya está escrita en el código, ya que no solo se imprime para una cierta hora. Después pasa a verificar por medio de los minutos, más adelante se explicarán con las funciones para los formatos. Por último, si no coincide con ningún if significa que, pasará al else, se imprimirá "O' clock" después de la hora, esto no requiere función porque solo es cuando la variable minuto es igual a 0.

# FORMATOS DE IMPRESIÓN
Ahora se explican las funciones para imprimir el texto de acuerdo al if o else que se haya seleccionado en la función principal.

  format_0():
    En este primer formato la estructura de la frase es la siguiente: " " one minute " + word + " " + hour ".
    # Variables de la función
    + word: se extrae la palabra de times[word]
    + hour: se obtiene el número en texto de number{hour} y para obtener la opción correcta, se valida en un if, si la hora es más de 12 se le restará 12 y si es menos que 12 se mantiene igual, y ese es el valor que retorna a la función.
  
   format_1():
    Esta estructura es la más común para poder determinar la frase, es la siguiente: " minute + " minutes " + word + " " + hour "; en este caso se tiene predeterminada la palabra minutes porque nunca cambia, y se tiene 3 variables.
    Variables
    + minute: esta variable es la que determina el valor de las otras dos, pues depende de lo siguiente:
        Si el minuto ingresado está entre 2 y 29, excluyendo a 15, el valor de la hora será la ingresada, y se usa la misma validación para saber si se le resta 12 a la hora ingresada, como se explicó en la función anterior, y también se debería usar "past" en la variable "word", pero si en lugar de que ingrese alguno de esos e ingresa un número entre 31 y 58, excluyendo a 45, al resultado de la validación de "hour" se le sumará 1 y ese valor se extraerá de numbers{} y "word" será "to".
    + hour: Dependiendo del minuto este será el mismo ingresado o se le sumará 1.
    + word: Es la palabra que se utilizará y será "past" o "to" de acuerdo al minuto ingresado.
  
 format_2():
    Su estructura es: " word_1 + " " + word_2 + " " + hour "; esta solo es más específica para cuando se ingresa en minutos: 15, 30 o 45.
    # Variables
    + word_1: Esta variable será "quarter", si el minuto es 15 o 45, o "half" si el minuto es 30.
    + word_2: La palabra será "past" si el minuto es 15 o 30, o "to" si el minuto es 45.
hour: Esta será la hora, pero primero se verifica si es menor o mayor a 12, y si el minuto es 15 o 30, el valor seguirá siendo el mismo que retorne la verificación, pero si el minuto es 45, a su valor retornado se le sumará 1.
