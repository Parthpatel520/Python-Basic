# Tiny Demo - Python Socket Client/Server

This project is a small TCP socket communication demo in Python.

## Project Structure

```text
Tiny Demo/
|-- client/
|   `-- client.py
|-- server/
|   `-- server.py
`-- README.md
```

## Requirements

- Python 3.x

## How to Run

1. Open terminal in project root:
   `d:\Parth\PARTH\Python\Tiny Demo`
2. Start the server:
   `python server/server.py`
3. Open another terminal and run the client:
   `python client/client.py`

## Expected Output

Server terminal:
- `Server waiting for connection...`
- `Connected to: (...)`
- `Client says: Hello Server`

Client terminal:
- `Server says: Hello Client`

## Notes

- Host: `localhost`
- Port: `5000`
- Make sure server starts before client.
