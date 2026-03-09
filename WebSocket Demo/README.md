# WebSocket Demo - Python

This is a simple Python WebSocket client-server demo using the `websockets` package.

## Project Structure

```text
WebSocket Demo/
|-- client/
|   `-- client.py
`-- Server/
    `-- server.py
```

## Requirements

- Python 3.8+

## Download / Install WebSocket Package

Run this before starting the demo:

```bash
pip install websockets
```

If your system uses `pip3`, use:

```bash
pip3 install websockets
```

## How to Run

1. Open terminal in `WebSocket Demo` folder.
2. Start the server:

```bash
python Server/server.py
```

3. Open a second terminal and run the client:

```bash
python client/client.py
```

## Expected Output

Server terminal:
- `Server running on ws://localhost:8765`
- `Client connected`
- `Received: Hello Server`

Client terminal:
- `Server says: Server received: Hello Server`

## Notes

- Host: `localhost`
- Port: `8765`
- Always start server first, then client.
