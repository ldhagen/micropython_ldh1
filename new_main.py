from network import ftp, telnet, STA_IF, WLAN
from machine import idle
from m5stack import machine
from m5stack import lcd
from time import strftime
import utime, upysh, m5stack
import _thread

rtc = machine.RTC()

def start_wifi():
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

def watch():
    while True:
        # start position for Date
        if not rtc.synced():                                                            # set color to sync status    
            lcd.setColor(lcd.RED)
        else: 
            lcd.setColor(lcd.GREEN)
#       lcd.setCursor(92, 227)                                                          # uncomment if you need date on display
#       lcd.print("Date {}".format(utime.strftime("%Y-%m-%d", utime.localtime())))      # uncomment if needed
        # start position for time only
        lcd.setCursor(213, 227)                                                         # uncomment if date active (see upper lines)
        lcd.print(" Time {}".format(utime.strftime('%H:%M:%S', utime.localtime())))
        utime.sleep(1)

def main():
    start_wifi()
    print('started wifi and tools')
    # move to lowest line on M5STACK display
    lcd.setCursor(0, 227)
    lcd.setColor(lcd.WHITE)
    lcd.print("RTC Clock 1")
    
    # initiate rtc
    print("Synchronize time from NTP server with TZ=US Central ...")
    rtc.ntp_sync(server="hr.pool.ntp.org", tz="CST6CDT5,M4.1.0/2,M10.5.0/2")  #https://prom-electric.ru/media/uclibc-zoneinfo-list.txt
    _thread.start_new_thread ("clock",watch, ())

if __name__ == '__main__':
    main()
