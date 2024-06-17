import http.server
import socketserver
import time

def main():
    #definir el port a on s'executara
    PORT = 9000

    #configurar el manejador de les solicituds HTTP
    handler=http.server.SimpleHTTPRequestHandler

    #crear l'objet del servidor
    httpd=socketserver.TCPServer(("", PORT), handler)

    print(f"servidor web funcionant en el port {PORT}")

    #def el temps de duracio en segons (5 min)
    duracio=5 * 60

    try:
        #iniciar el servidor i esperar durant el temps especificat
        httpd.serve_forever()
        time.sleep(duracio)
    except KeyboardInterrupt:
        pass

    # tancar el servidor despres de que hagi passat el temps de duració
    http.shutdown()
    print(f"Servidor web detingut despres de {duracio} segons")

def pex6():
    main()