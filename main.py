from network import ftp, telnet, STA_IF, WLAN
from machine import idle
def main():
    wlan = WLAN(STA_IF)
    wlan.active(True)
    nets = wlan.scan()
    for net in nets:
        ssid = net[0]
        if ssid == b'Jxxxxxxxxxe':
            wlan.connect(ssid, 'xxxxxxxx')
            while not wlan.isconnected():
                idle() # save power while waiting
            print('WLAN connection succeeded!')
            ftp.start(user='l******', password='*****')
            telnet.start(user='l******', password='*****')
            break

if __name__ == '__main__':
    main()
