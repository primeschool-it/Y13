import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.settimeout(5)
list_of_websites = ['realpython.com','chargesurfing.tkopen.com','google.com' ,'facebook.com', 'yahoo.com.br', 'microsoft.com', 'tkopen.com']

def port_scanner(website):
    ip = socket.gethostbyname(website)
    print("#############################")
    print("SCANNING port for ....... %s:%s" % (website,ip))
    for port in range(0, 60000):
        time.sleep(.1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print("[+] port %s is open" % port)
        else:
            print (result)
            # print("[-] port %s is closed" % port)
    return True

for website in list_of_websites:
    port_scanner(website)
sock.close()
