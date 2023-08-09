import socket

def test_radius_connection(server_ip, server_port):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Set a timeout for the socket (optional)
    udp_socket.settimeout(5)  # Set a timeout of 5 seconds
    
    try:
        # Send a RADIUS request packet to the server
        radius_request = b'\x01\x02\x00\x20' + 16 * b'\x00'  # Example RADIUS packet
        udp_socket.sendto(radius_request, (server_ip, server_port))
        
        # Receive a response from the server (optional)
        response, address = udp_socket.recvfrom(1024)
        
        print("Connection to RADIUS server successful.")
    except socket.error as e:
        print("Error: Connection to RADIUS server failed:", e)
    finally:
        udp_socket.close()

if __name__ == "__main__":
    radius_server_ip = "127.0.0.1"  # Change this to the actual RADIUS server IP
    radius_server_port = 1812
    
    test_radius_connection(radius_server_ip, radius_server_port)
