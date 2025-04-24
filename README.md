# clientserverchatprezy


# Re-running the code block after code execution state reset
readme_content = """
# Client-Server Chat System

This is a Python-based client-server chat system developed for the SDI 3203: Network Fundamentals term project. It allows users to communicate in real time over a local network using socket programming.

## 📚 Project Overview
- **Course**: SDI 3203 – Network Fundamentals
- **Instructor**: Dr. Chenggang Wang
- **Project Goal**: Create a push-based messaging system using TCP sockets.
- **Team Members**: John Doe & Jane Smith

## 🧠 Features
- Unique user registration with the server
- Real-time message delivery using TCP sockets
- Online user list with the `server:who` command
- Graceful exit with the `server:exit` command
- Basic multi-threading for handling concurrent clients

## 🗂 File Structure
- `server.py`: The main server that handles incoming client connections.
- `client.py`: A simple client that connects to the server and sends/receives messages.

## ▶️ How to Run in GitHub Codespaces

### 1. **Create and Open a Codespace**
- Push this project to a GitHub repository.
- Open the repo in a Codespace by clicking **Code > Codespaces > New codespace**.

### 2. **Start the Server**
In the first terminal:
```bash
python3 server.py
