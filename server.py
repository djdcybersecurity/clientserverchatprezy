import socket
import threading

# A sacred scroll to track online warriors (users)
users = {}

def handle_client(client_socket, addr):
    try:
        # First rule of chat club: choose a username!
        username = client_socket.recv(1024).decode().strip()
        if username in users:
            client_socket.send("Username already taken. Pick something cooler.".encode())
            client_socket.close()
            return
        users[username] = client_socket
        client_socket.send(f"Welcome {username}! You're live.".encode())

        while True:
            data = client_socket.recv(1024).decode()
            if data == "server:who":
                # Spill the tea on who's online
                online = ", ".join(users.keys())
                client_socket.send(f"Online users: {online}".encode())
            elif data == "server:exit":
                # Peace out!
                client_socket.send("Disconnecting... See ya!".encode())
                break
            else:
                # Texting logic — old school, like AIM but nerdier
                if ":" in data:
                    recipient, msg = data.split(":", 1)
                    if recipient in users:
                        users[recipient].send(f"{username}: {msg}".encode())
                    else:
                        client_socket.send("That user vanished into the void.".encode())
    finally:
        # The user has left the chat (literally)
        del users[username]
        client_socket.close()

def start_server(port=8080):
    # Plugging in the magical chat gateway
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen()
    print(f"Server started on port {port}. Time to mingle.")

    while True:
        client_socket, addr = server_socket.accept()
        # One client = one thread = one great adventure
        threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True).start()

if __name__ == "__main__":
    start_server()
