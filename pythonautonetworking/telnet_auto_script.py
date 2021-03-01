import sys
import getpass
from telnetlib import Telnet

script = sys.argv[0]
config_file = sys.argv[1]
host = sys.argv[2]
user = input("Enter your telnet username: ")
password = getpass.getpass()
def telnet_auto_config():
    with Telnet(host, 23) as tn:
        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
        
        config_file = open('config','r')
        
        for line in config_file:
            tn.write(line.encode("ascii")+b"\r\n")
    
        config_file.close()
        print(tn.read_all().decode('ascii'))

def main():
    telnet_auto_config()
    
if __name__=="__main__":
    try:
        main()
    except:
        print ("Trigger Exception, traceback info forward to log file.")
        traceback.print_exc(file=open("/var/log/err.log","w"))
        sys.exit(1)