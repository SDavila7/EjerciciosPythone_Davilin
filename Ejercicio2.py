perimetro=float #En esta línea se define la variable "perímetro" como "float" ya que el perimetro se puede dar en decimales y/o enteros
altura=float #En esta línea se define la variable "altura" como "float" ya que la altura se puede dar en decimales y/o enteros
base=float(input("Cuál es el valor de la base del rectángulo: ")) #En esta línea se pregunta por el valor de la base del rectángulo y se guarda el valor en la variable "base"
altura=float(input("Cuál es el valor de la altura del rectángulo: ")) #En esta línea se pregunta por el valor de la altura del rectángulo y se guarda el valor en la variable "altura"
perimetro=base*2+altura*2 #En esta línea se realiza la operación para hallar el perímetro del rectangulo, sumando todos los lados
area= base*altura #En esta línea se realiza la operación para hallar el área del rectangulo, multiplicando base por altura
print("El perimetro del rectángulo es",perimetro,"y el área es",area) #Se muestra la respuesta del programa,mostrando el perímetro y el área