import requests

ip_list = ["192.168.1.1", "192.168.3.2", "192.168.5.3", "192.168.4.4", "192.168.6.5", "192.168.7.6"]

for ip in ip_list:
    headers = {"X-Forwarded-For": ip}
    response = requests.get('http://localhost:8061', headers=headers)
    server_instance = response.headers.get('X-Server-Instance', 'Desconocido')
    print(f"IP: {ip}, Servidor: {server_instance}")