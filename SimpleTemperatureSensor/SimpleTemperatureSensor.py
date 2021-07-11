import habcatev,time
import re 
import RPi.GPIO as GPIO

class SimpleTemperatureSensor(habcatev.device.Device.Device):
    def __init__(self):
        super(SimpleTemperatureSensor, self).__init__()

    def init(self):
        self.log.logger.error("Iniciando ...")
        self.setSubscriptionArr([self.config['topics']['input']])
        self.pin = self.config['pin']
        self.sequence = self.config['sequence'].split(',')
        self.state = self.config['initialState'].upper()
        GPIO.setup(self.pin, GPIO.OUT)
       
    def on_event(self,topic,data):
        print('Event')
        
    def loop(self):
        print('Running')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
SimpleTemperatureSensor()