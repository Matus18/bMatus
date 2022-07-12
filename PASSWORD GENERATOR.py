import random

lower ="abcdefghijklmnopqrstuvwyz"
upper = "ABCDEFGHIGKLMNOPQRSTUVWYZ"
numbers = "0123456789"
symbols = "[]}{()*;/_-"

all = lower + upper + numbers + symbols

lenght = 8  #COLOCAR LA LONGITUD DE LA CLAVE QUE DESEA
password = " ".join(random.sample(all, lenght))
print(password)
