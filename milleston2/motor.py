import pigpio
import time
servo = 12
pwm = pigpio.pi() 
def motor_init():

    pwm.set_mode(servo, pigpio.OUTPUT)
    pwm.set_PWM_frequency(servo, 50)
    pwm.set_PWM_range(servo, 20000) # 1,000,000 / 50 = 20,000us for 100% duty cycle

def motor_angle(ang):
    pwm.hardware_PWM(servo, 50, 30000+ang*500)