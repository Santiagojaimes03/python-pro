import random

caracter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int (input ("¿que tamaño quieres que sea tu contraseña?"))
contra = ""
for i in range(longitud):
    contra += random.choice(caracter)
print (contra)
