import time
from grove.grove_ryb_led_button import GroveLedButton
 
def main(port):
    
    ledbtn = GroveLedButton(port)
    i=1
    time_sleep=2
    while True and i<4:
        ledbtn.led.light(True)
        print('turn on LED ')
        time.sleep(time_sleep)
        
        ledbtn.led.light(False)
        print('turn off LED ')
        time.sleep(time_sleep)
        i=i+1


if __name__ == '__main__':
    main(5)
    
    
    

