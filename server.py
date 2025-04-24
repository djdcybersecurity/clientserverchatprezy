# server.py
import socket
import threading

# Our mighty ledger of who's in the chat room
users = {}

def handle_client(client_socket, addr):
    try:
        # First rule of chat club: claim your name
        username = client_socket.recv(1024).decode().strip()
        if username in users:
            client_socket.send("Username already taken. Try something unique.".encode())
            client_socket.close()
            return

        users[username] = client_socket
        client_socket.send(f"Welcome {username}! You've entered the chat arena.".encode())

        while True:
            data = client_socket.recv(1024).decode()
            if data == "server:who":
                # Who's in this digital clubhouse?
                online = ", ".join(users.keys())
                client_socket.send(f"Online users: {online}".encode())

            elif data == "server:exit":
                # This one is signing off
                client_socket.send("Disconnecting. You’ll be missed.".encode())
                break

            else:
                # Basic format: recipient:message
                if ":" in data:
                    recipient, msg = data.split(":", 1)
                    if recipient in users:
                        users[recipient].send(f"{username}: {msg}".encode())
                    else:
                        client_socket.send("That user has vanished into the internet void.".encode())
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        # Clear them from the party when they leave
        if username in users:
            del users[username]
        client_socket.close()

def start_server(port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(5)
    print(f"Server is up and running on port {port}. Let the chatting commence.")

    while True:
        client_socket, addr = server_socket.accept()
        # Spinning up a fresh thread for this lucky newcomer
        threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True).start()

if __name__ == "__main__":
    start_server()
