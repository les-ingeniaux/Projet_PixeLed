import utilitairesLed
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
    <title>PixeLed</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: #e2e8f0;
            text-align: center;
            margin: 0;
            padding: 40px;
        }

        h1 {
            margin-bottom: 30px;
        }

    .btn {
        display: inline-block;
        background: linear-gradient(145deg, #3b82f6, #1d4ed8);
        color: white;
        border: none;
        padding: 18px 30px;
        margin: 12px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 16px;

        cursor: pointer;
        transition: all 0.15s ease-in-out;

        box-shadow: 0 6px 0 #1e3a8a;
        transform: translateY(0);
        min-width: 160px;
    }

    .btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 0 #1e3a8a;
    }

    .btn:active {
        transform: translateY(4px);
        box-shadow: 0 2px 0 #1e3a8a;
    }

    .btn.active {
        background: linear-gradient(145deg, #22c55e, #16a34a);
        box-shadow: 0 6px 0 #14532d;
    }
    
        .panel {
            background: #1e293b;
            padding: 20px;
            margin: 20px;
            border-radius: 15px;
            display: inline-block;
        }

        #status {
            margin-top: 20px;
            font-size: 18px;
            color: #38bdf8;
        }
    </style>
</head>
<body>

    <h1>Centre de commandes du PixeLed</h1>
    <div class="panel">
        <button class ="btn" onclick="setAllumage(0)">PixeLed OFF</button>
        <button class ="btn" onclick="setAllumage(1)">PixeLed ON</button>
    </div>
    <div class="panel">
        <button class ="btn" onclick="setImage(1)">Image 1</button>
        <button class ="btn" onclick="setImage(2)">Image 2</button>
        <button class ="btn" onclick="setImage(3)">Image 3</button>
    </div>
    <script>
        function setAllumage(n) {
            fetch('/set?allumage=' + n);
        }
    </script>
    <script>
        function setImage(n) {
            fetch('/set?image=' + n);
        }
    </script>
</body>
</html>
"""

def connect(ssid,password): 
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


def init():
    global s
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.bind(addr)
    except OSError:
        print("Port busy, resetting...")
        import machine
        machine.reset()
    s.listen(1)
    s.setblocking(False)
    print("Serveur web actif sur le port 80")

def poll():
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
        
        if "?image=" in path:
            #print("setting anim")
            try:
                image = int(path.split("image=")[1].split("&")[0])
                print(image)
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