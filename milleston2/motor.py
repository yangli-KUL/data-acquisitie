import pigpio
import time

servo = 12
 
pwm = pigpio.pi() 
pwm.set_mode(servo, pigpio.OUTPUT)
 
pwm.set_PWM_frequency(servo, 50)
pwm.set_PWM_range(servo, 20000) # 1,000,000 / 50 = 20,000us for 100% duty cycle

for i in range(20,50):
    pwm.hardware_PWM(servo, 50, 2000*i)
    time.sleep(1)
pwm.set_servo_pulsewidth(servo, 0)