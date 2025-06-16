import socket
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("socket created")
    #sender ke ander ip add receivr ka he aayega hamesha and receiver ka hi aayega khud ka
    ip_add = "192.168.154.1"
    port = 8887
    complete_add = (ip_add,port)
    s.bind(complete_add)

    while True:
        message , sender_address = s.recvfrom(1024)

        print("Raw Message", message)
        print("Sender Message", sender_address)

        decoded_msg = message.decode("ascii")
        print("Message",decoded_msg)

except Exception as e:
    print("An Eroor occured",e)
