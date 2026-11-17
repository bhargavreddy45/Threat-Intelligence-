
# Track established outbound connections
connections = set()

def outbound(source, destination, port):
    connection = (source, destination, port)
    connections.add(connection)

    print("Outbound connection ALLOWED")
    print("Connection recorded:", connection)

def inbound(source, destination, port):
    # Check whether this is return traffic
    connection = (destination, source, port)

    if connection in connections:
        print("Inbound return traffic ALLOWED")
    else:
        print("Inbound traffic BLOCKED")

# Simulate network traffic
outbound("Client", "WebServer", 443)

inbound("WebServer", "Client", 443)
inbound("UnknownHost", "Client", 22)
