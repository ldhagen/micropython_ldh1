# RTC Clock with NTP Sync for M5STACK
# References:
# https://forum.micropython.org/viewtopic.php?t=4329
# Lobo Version to init RTC and timezone
# https://forum.micropython.org/viewtopic.php?f=18&t=3553&p=21616&hilit=timezone#p21616
from m5stack import machine
from m5stack import lcd
from time import strftime
import utime
import _thread

# move to lowest line on M5STACK display
lcd.setCursor(0, 227)
lcd.setColor(lcd.WHITE)
lcd.print("RTC Clock 1")

# initiate rtc
rtc = machine.RTC()
print("Synchronize time from NTP server with TZ=US Central ...")
rtc.ntp_sync(server="hr.pool.ntp.org", tz="CST6CDT5,M4.1.0/2,M10.5.0/2")  #https://prom-electric.ru/media/uclibc-zoneinfo-list.txt

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

_thread.start_new_thread ("clock",watch, ())
