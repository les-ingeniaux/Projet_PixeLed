import machine 
import network 
import socket 
from time import sleep
import neopixel

ssid = 'Salle_Alan'
password = 'IngX27rpG#$'

def connect(): 
  # Connexion au WLAN 
  mon_reseau_wifi = network.WLAN(network.STA_IF)
  mon_reseau_wifi.active(True) #Active la connection wifi
  mon_reseau_wifi.connect(ssid, password)
  while (mon_reseau_wifi.isconnected() == False) :
      print(mon_reseau_wifi.isconnected())
      print("En attente de connexion...")
      print("\n")
      sleep(2)     
  ip = mon_reseau_wifi.ifconfig()[0] 
  print(f'Connecté sur {ip}') 
  return ip 

def open_socket():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print("Serveur web actif sur le port 80")
    return s

def webpage(state): 
  # Modèle HTML 
  html = f""" 
      <!DOCTYPE html> 
      <html>
      <body>
      <form action="./lighton"> 
      <input type="submit" value="Lumiere allumee" /> 
      </form> 
      <form action="./lightoff"> 
      <input type="submit" value="Lumiere eteinte" /> 
      </form>
      </form> 
      <form action="./lightalternee"> 
      <input type="submit" value="Lumiere alternee" /> 
      </form>
      <p>La LED est {state}</p> 
      </body> 
      </html> 
      """ 
  return str(html)


def serve(connection):
    state = 'OFF'
    matrice_off()

    while True:
        client, addr = connection.accept()
        request = client.recv(1024).decode()

        print("Requête :", request)

        if 'GET /lighton' in request:
            matrice_on()
            state = 'ON'

        elif 'GET /lightoff' in request:
            matrice_off()
            state = 'OFF'
            
        elif 'GET /lightalternee' in request:
            matrice_alternee()
            state = 'Alternee'

        html = webpage(state)

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "Connection: close\r\n"
            "\r\n" + html
        )

        client.sendall(response.encode())
        client.close()


try:
    ip = connect()
    connection = open_socket()
    serve(connection) 
except KeyboardInterrupt: 
    machine.reset()