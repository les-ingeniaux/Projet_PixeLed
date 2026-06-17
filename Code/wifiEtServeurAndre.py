"""
Ce module gère la connexion au wifi et le serveur web qui reçoit les commandes de la page web
pour les stocker dans des variables accessibles dans main.py
C'est également dans ce module que se trouve le code de la page web elle-même, que vous pouvez modifier à votre guise pour ajouter
le nombre de boutons que vous souhaitez, ou pour changer le style de la page.
"""  

import machine
import network
import socket
from time import sleep
import state
   
HTML_PAGE = """\
HTTP/1.1 200 OK\r
Content-Type: text/html\r
\r
<!DOCTYPE html>
<html>
<head>
    <style>
        canvas {
            border: 1px solid #000000;
            cursor: pointer;
        }
    </style>
</head>
<body>

<canvas id="myCanvas" width="200" height="200"></canvas>

<canvas id="myCanvas2" width="200" height="200"></canvas>

<script>

var c1 = document.getElementById("myCanvas");
var ctx1 = c1.getContext("2d");


ctx1.moveTo(0, 25); ctx1.lineTo(200, 25); ctx1.stroke();
ctx1.moveTo(0, 50); ctx1.lineTo(200, 50); ctx1.stroke();
ctx1.moveTo(0, 75); ctx1.lineTo(200, 75); ctx1.stroke();
ctx1.moveTo(0, 100); ctx1.lineTo(200, 100); ctx1.stroke();
ctx1.moveTo(0, 125); ctx1.lineTo(200, 125); ctx1.stroke();
ctx1.moveTo(0, 150); ctx1.lineTo(200, 150); ctx1.stroke();
ctx1.moveTo(0, 175); ctx1.lineTo(200, 175); ctx1.stroke();


ctx1.moveTo(25, 0); ctx1.lineTo(25, 200); ctx1.stroke();
ctx1.moveTo(50, 0); ctx1.lineTo(50, 200); ctx1.stroke();
ctx1.moveTo(75, 0); ctx1.lineTo(75, 200); ctx1.stroke();
ctx1.moveTo(100, 0); ctx1.lineTo(100, 200); ctx1.stroke();
ctx1.moveTo(125, 0); ctx1.lineTo(125, 200); ctx1.stroke();
ctx1.moveTo(150, 0); ctx1.lineTo(150, 200); ctx1.stroke();
ctx1.moveTo(175, 0); ctx1.lineTo(175, 200); ctx1.stroke();

ctx1.fillStyle = "black";
ctx1.fillRect(0, 0, 200, 200);

var c2 = document.getElementById("myCanvas2");
var ctx2 = c2.getContext("2d");

ctx2.fillStyle = "black"; ctx2.fillRect(0, 0, 25, 25);
ctx2.fillStyle = "#005500"; ctx2.fillRect(0, 25, 25, 25);
ctx2.fillStyle = "#00aa00"; ctx2.fillRect(0, 50, 25, 25);
ctx2.fillStyle = "#00ff00"; ctx2.fillRect(0, 75, 25, 25);
ctx2.fillStyle = "#550000"; ctx2.fillRect(0, 100, 25, 25);
ctx2.fillStyle = "#555500"; ctx2.fillRect(0, 125, 25, 25);
ctx2.fillStyle = "#55aa00"; ctx2.fillRect(0, 150, 25, 25);
ctx2.fillStyle = "#55ff00"; ctx2.fillRect(0, 175, 25, 25);

ctx2.fillStyle = "#aa0000"; ctx2.fillRect(25, 0, 25, 25);
ctx2.fillStyle = "#aa5500"; ctx2.fillRect(25, 25, 25, 25);
ctx2.fillStyle = "#aaaa00"; ctx2.fillRect(25, 50, 25, 25);
ctx2.fillStyle = "#aaff00"; ctx2.fillRect(25, 75, 25, 25);
ctx2.fillStyle = "#ff0000"; ctx2.fillRect(25, 100, 25, 25);
ctx2.fillStyle = "#ff5500"; ctx2.fillRect(25, 125, 25, 25);
ctx2.fillStyle = "#ffaa00"; ctx2.fillRect(25, 150, 25, 25);
ctx2.fillStyle = "#ffff00"; ctx2.fillRect(25, 175, 25, 25);

ctx2.fillStyle = "#000055"; ctx2.fillRect(50, 0, 25, 25);
ctx2.fillStyle = "#005555"; ctx2.fillRect(50, 25, 25, 25);
ctx2.fillStyle = "#00aa55"; ctx2.fillRect(50, 50, 25, 25);
ctx2.fillStyle = "#00ff55"; ctx2.fillRect(50, 75, 25, 25);
ctx2.fillStyle = "#550055"; ctx2.fillRect(50, 100, 25, 25);
ctx2.fillStyle = "#555555"; ctx2.fillRect(50, 125, 25, 25);
ctx2.fillStyle = "#55aa55"; ctx2.fillRect(50, 150, 25, 25);
ctx2.fillStyle = "#55ff55"; ctx2.fillRect(50, 175, 25, 25);

ctx2.fillStyle = "#aa0055"; ctx2.fillRect(75, 0, 25, 25);
ctx2.fillStyle = "#aa5555"; ctx2.fillRect(75, 25, 25, 25);
ctx2.fillStyle = "#aaaa55"; ctx2.fillRect(75, 50, 25, 25);
ctx2.fillStyle = "#aaff55"; ctx2.fillRect(75, 75, 25, 25);
ctx2.fillStyle = "#ff0055"; ctx2.fillRect(75, 100, 25, 25);
ctx2.fillStyle = "#ff5555"; ctx2.fillRect(75, 125, 25, 25);
ctx2.fillStyle = "#ffaa55"; ctx2.fillRect(75, 150, 25, 25);
ctx2.fillStyle = "#ffff55"; ctx2.fillRect(75, 175, 25, 25);

ctx2.fillStyle = "#0000aa"; ctx2.fillRect(100, 0, 25, 25);
ctx2.fillStyle = "#0055aa"; ctx2.fillRect(100, 25, 25, 25);
ctx2.fillStyle = "#00aaaa"; ctx2.fillRect(100, 50, 25, 25);
ctx2.fillStyle = "#00ffaa"; ctx2.fillRect(100, 75, 25, 25);
ctx2.fillStyle = "#5500aa"; ctx2.fillRect(100, 100, 25, 25);
ctx2.fillStyle = "#5555aa"; ctx2.fillRect(100, 125, 25, 25);
ctx2.fillStyle = "#55aaaa"; ctx2.fillRect(100, 150, 25, 25);
ctx2.fillStyle = "#55ffaa"; ctx2.fillRect(100, 175, 25, 25);

ctx2.fillStyle = "#aa00aa"; ctx2.fillRect(125, 0, 25, 25);
ctx2.fillStyle = "#aa55aa"; ctx2.fillRect(125, 25, 25, 25);
ctx2.fillStyle = "#aaaaaa"; ctx2.fillRect(125, 50, 25, 25);
ctx2.fillStyle = "#aaffaa"; ctx2.fillRect(125, 75, 25, 25);
ctx2.fillStyle = "#ff00aa"; ctx2.fillRect(125, 100, 25, 25);
ctx2.fillStyle = "#ff55aa"; ctx2.fillRect(125, 125, 25, 25);
ctx2.fillStyle = "#ffaaaa"; ctx2.fillRect(125, 150, 25, 25);
ctx2.fillStyle = "#ffffaa"; ctx2.fillRect(125, 175, 25, 25);

ctx2.fillStyle = "#0000ff"; ctx2.fillRect(150, 0, 25, 25);
ctx2.fillStyle = "#0055ff"; ctx2.fillRect(150, 25, 25, 25);
ctx2.fillStyle = "#00aaff"; ctx2.fillRect(150, 50, 25, 25);
ctx2.fillStyle = "#00ffff"; ctx2.fillRect(150, 75, 25, 25);
ctx2.fillStyle = "#5500ff"; ctx2.fillRect(150, 100, 25, 25);
ctx2.fillStyle = "#5555ff"; ctx2.fillRect(150, 125, 25, 25);
ctx2.fillStyle = "#55aaff"; ctx2.fillRect(150, 150, 25, 25);
ctx2.fillStyle = "#55ffff"; ctx2.fillRect(150, 175, 25, 25);

ctx2.fillStyle = "#aa00ff"; ctx2.fillRect(175, 0, 25, 25);
ctx2.fillStyle = "#aa55ff"; ctx2.fillRect(175, 25, 25, 25);
ctx2.fillStyle = "#aaaaff"; ctx2.fillRect(175, 50, 25, 25);
ctx2.fillStyle = "#aaffff"; ctx2.fillRect(175, 75, 25, 25);
ctx2.fillStyle = "#ff00ff"; ctx2.fillRect(175, 100, 25, 25);
ctx2.fillStyle = "#ff55ff"; ctx2.fillRect(175, 125, 25, 25);
ctx2.fillStyle = "#ffaaff"; ctx2.fillRect(175, 150, 25, 25);
ctx2.fillStyle = "#ffffff"; ctx2.fillRect(175, 175, 25, 25);





var couleurSelectionnee = "rgb(0,0,0)";


c2.addEventListener("click", function(event) {

    var rect = c2.getBoundingClientRect();
    var x = event.clientX - rect.left;
    var y = event.clientY - rect.top;
    var pixelData = ctx2.getImageData(x, y, 1, 1).data;
   

    couleurSelectionnee = "rgb(" + pixelData[0] + "," + pixelData[1] + "," + pixelData[2] + ")";
});

c1.addEventListener("click", function(event) {

    var rect = c1.getBoundingClientRect();
    var x = event.clientX - rect.left;
    var y = event.clientY - rect.top;

    var caseX = Math.floor(x / 25) * 25;
    var caseY = Math.floor(y / 25) * 25;


    ctx1.fillStyle = couleurSelectionnee;
    ctx1.fillRect(caseX, caseY, 25, 25);

    ctx1.strokeStyle = "black";
    ctx1.strokeRect(caseX, caseY, 25, 25);
   
//Evoyer x ; y ; couleurSelectionnee
setCoordonee(caseX/25,caseY/25)
setColor(couleurSelectionnee);

});

function setColor(couleurAEnvoyer)
{
console.log(couleurAEnvoyer);
    fetch('/set?couleur=' + couleurAEnvoyer);
   
}

function setCoordonee(x,y)
{
console.log(x);
console.log(y);
    fetch('/set?coordonee=' + x +"," + y);
   
}    
   
</script>

</body>
</html>

"""


"""
Cette fonction se connecte au réseau Wi-Fi avec le ssid et le mot de passe fournis en argument.
"""
def connect(ssid,password)->None:
  mon_reseau_wifi = network.WLAN(network.STA_IF)
  mon_reseau_wifi.active(True)
  mon_reseau_wifi.connect(ssid, password)
  while (mon_reseau_wifi.isconnected() == False) :
      print(mon_reseau_wifi.isconnected())
      print("En attente de connexion...")
      print("\n")
      sleep(2)    
  ip = mon_reseau_wifi.ifconfig()[0]
  print(f'Connecté sur {ip}')


"""
Cette fonction initialise le serveur web et le rend prêt à recevoir des commandes de la page web
"""
def init()->None:
    global s
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.bind(addr)
    except OSError:
        print("Port busy, resetting...")
        machine.reset()
    s.listen(1)
    s.setblocking(False)
    print("Serveur web actif sur le port 80")

"""
Cette fonction vérifie si des requêtes sont disponibles sur le socket du serveur web : il faut l'appeler régulièrement dans la boucle principale de main.py pour que les commandes de la page web soient prises en compte
"""
def poll()->None:
    try:
        cl, addr = s.accept()
    except OSError as e:
        if e.args[0] == errno.EAGAIN:
            return
        else:
            print("Socket error:", e)
            return

    #print("Client connected from", addr)

    try:
        cl.setblocking(True)
        request = cl.recv(1024).decode()
        request_line = request.split("\r\n")[0]
        path = request_line.split(" ")[1]
        print(path)
        if "?allumage=" in path:
            #print("setting toggle")
            try:
                toggle = int(path.split("allumage=")[1].split("&")[0])
                #print(toggle)
                state.allumage = toggle
            except:
                pass
           
            response = "HTTP/1.1 200 OK\r\n\r\nOK"
            cl.send(response.encode())
            cl.close()
            return
       
        if "?couleur=" in path:
            #print("setting anim")
            try:
                rgb = path.split("couleur=rgb(")[1]
                valeurs = rgb.split(",")
                state.rouge = int(valeurs[0])
                state.vert = int(valeurs[1])
                state.bleu = int(valeurs[2].split(")")[0])
                #print(rgb)
                #print(rouge)
                #print(vert)
                #print(bleu)
                state.imageActuelle = image
            except:
                pass

            response = "HTTP/1.1 200 OK\r\n\r\nOK"
            cl.send(response.encode())
            cl.close()
            return
        cl.send(HTML_PAGE)
               
               
        if "?coordonee=" in path:
            #print("setting anim")
            #print(path)
            try:
                state.x=int(path.split("coordonee=")[1].split(",")[0])
                state.y=int(path.split("coordonee=")[1].split(",")[1])
                print(state.x,state.y)
                state.imageActuelle = image
            except:
                pass

            response = "HTTP/1.1 200 OK\r\n\r\nOK"
            cl.send(response.encode())
            cl.close()
            return
        cl.send(HTML_PAGE)

    except Exception as e:
        print("Error handling request:", e)
        pass

    finally:
        cl.close()
