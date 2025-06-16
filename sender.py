import socket

try:
    ##creating socket:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ##dgram --- datagram
    print("socket created")
    ip_add = "192.168.154.1"
    port = 8887
    target_add = (ip_add,port)
    message = input("Enter the message : 😊 ")
    encoded_msg = message.encode("ascii")
    s.sendto(encoded_msg,target_add)
    print("message sent successfully")
    s.close()

except Exception as e:
    print("an error occured",e)