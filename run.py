from app import app
import socket

hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)  

if __name__ == "__main__":
    app.debug = True
    app.run(debug=True, host='0.0.0.0')
