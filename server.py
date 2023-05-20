from socket  import *
from constCS import * #-
import json

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-

print("Servidor iniciado")
resultado = 0

(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped
  json_data = json.loads(data)

  if json_data['operacao']  == 1:
     resultado = json_data['valor1'] + json_data['valor2']
  elif json_data['operacao']  == 2:
     resultado = json_data['valor1'] - json_data['valor2']
  elif json_data['operacao']  == 3:
     resultado = json_data['valor1'] * json_data['valor2']
  elif json_data['operacao']  == 4:
     resultado = json_data['valor1'] / json_data['valor2']
  print(str(resultado))
  conn.send(bytes(str.encode(str(resultado)))) # return sent
conn.close()               # close the connection
