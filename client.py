import socket
import threading

def listen_for_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print(msg)
        except:
            # Connection died — probably stepped on a LAN cable
            break

def start_client(server_ip="127.0.0.1", port=8080):
    # Reach out and touch... the server!
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, port))

    username = input("Choose your legendary username: ").strip()
    sock.send(username.encode())

    # We’re multitasking now! One thread for ears (listener), one for mouth (input)
    threading.Thread(target=listen_for_messages, args=(sock,), daemon=True).start()

    while True:
        msg = input()
        if msg.lower() == "exit":
            # Hit the eject button
            sock.send("server:exit".encode())
            break
        elif msg.lower() == "who":
            # Who’s in the digital room?
            sock.send("server:who".encode())
        else:
            # Type like a boss
            sock.send(msg.encode())

    # Closing time. Every client has to go home
    sock.close()

if __name__ == "__main__":
    start_client()
