# client.py
import socket
import threading

def listen_for_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print(msg)
        except:
            # You either disconnected or tripped over a virtual cable
            break

def start_client(server_ip="127.0.0.1", port=8080):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, port))

    username = input("Choose your legendary username: ").strip()
    sock.send(username.encode())

    # One thread is all ears; the other is all talk
    threading.Thread(target=listen_for_messages, args=(sock,), daemon=True).start()

    while True:
        msg = input()
        if msg.lower() == "exit":
            sock.send("server:exit".encode())
            break
        elif msg.lower() == "who":
            sock.send("server:who".encode())
        else:
            # Standard syntax: <recipient>:<message>
            sock.send(msg.encode())

    # Show’s over, closing the curtains
    sock.close()

if __name__ == "__main__":
    start_client()
