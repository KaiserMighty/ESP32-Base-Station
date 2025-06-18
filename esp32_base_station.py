import socket
import importlib

UDP_PORT = 17388
BUFFER_SIZE = 1024

COMMAND_MAP = {
    "DOORBELL_KNOCK": ("handlers.doorbell", "ring_bell"),
}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", UDP_PORT))

print(f"Listening for UDP packets on port {UDP_PORT}...")

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    raw_message = data.decode().strip()
    print(f"Received from {addr}: {raw_message}")

    if ":" in raw_message:
        command, arg = raw_message.split(":", 1)
        arg = arg.strip()
    else:
        command = raw_message
        arg = None

    command = command.strip()

    if command in COMMAND_MAP:
        module_name, function_name = COMMAND_MAP[command]
        try:
            module = importlib.import_module(module_name)
            func = getattr(module, function_name)

            if arg is not None:
                func(arg)
            else:
                func()

        except Exception as e:
            print(f"Error calling handler for '{command}': {e}")
    else:
        print(f"No handler for message: '{command}'")
