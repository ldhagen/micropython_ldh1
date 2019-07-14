from network import ftp, telnet, STA_IF, WLAN
from machine import idle
def main():
    wlan = WLAN(STA_IF)
    wlan.active(True)
    nets = wlan.scan()
    for net in nets:
        ssid = net[0]
        if ssid == b'JudiandLance':
            wlan.connect(ssid, 'balloon1')
            while not wlan.isconnected():
                idle() # save power while waiting
            print('WLAN connection succeeded!')
            ftp.start(user='ldhagen', password='ldhagen')
            telnet.start(user='ldhagen', password='ldhagen')
            break

if __name__ == '__main__':
    main()
