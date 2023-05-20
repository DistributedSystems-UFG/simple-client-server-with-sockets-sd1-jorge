from socket  import *
from constCS import * #-
import json

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)

print("\n Operações disponíveis: \n")
print(" [1] - Adição")
print(" [2] - Subtração")
print(" [3] - Multiplicação")
print(" [4] - Divisão")
print(" [5] - Sair")

while (True):  
  
  operacao = int(input("\n → Qual operação deseja realizar: [1][2][3][4][5]: "))
  if operacao == 5:
	  break
  valor1 = float(input(" Digite o primeiro valor: "))
  valor2 = float(input(" Digite o segundo valor: "))
  
  json_object = {"operacao": operacao, "valor1": valor1, "valor2": valor2}
  data = json.dumps(json_object)
  s.send(data.encode())
  
  data = s.recv(1024)     # receive the response
  print ("Resultado : " + bytes.decode(data))            # print the result

print("FIM")
s.close()               # close the connection
