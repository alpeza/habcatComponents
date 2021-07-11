import habcatev,time
import random 
import RPi.GPIO as GPIO

class SimpleWrite(habcatev.device.Device.Device):
    def __init__(self):
        super(SimpleWrite, self).__init__()

    def init(self):
        self.setSubscriptionArr([self.config['topics']['input']])
        self.state = self.config['initialState']
        self.pin = self.config['pin']

        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, self.state)

    def on_event(self,topic,data):
        if data.upper() == 'ON':
            self.log.logger.info("ON")
            GPIO.output(self.pin, True)
            self.state = True
            self.send(self.config['topics']['output'], str(self.state))
        elif data.upper() == 'OFF':
            self.log.logger.info("OFF")
            GPIO.output(self.pin, False)
            self.state = False
            self.send(self.config['topics']['output'], str(self.state))
        elif data.upper() == 'SWITCH':
            self.log.logger.info("SWITCH")
            self.state = not self.state
            GPIO.output(self.pin, self.state)
            self.send(self.config['topics']['output'], str(self.state))
        elif data.upper() == 'STATE':
            self.log.logger.info("STATE")
            self.send(self.config['topics']['output'], str(self.state))
        else:
            self.log.logger.error("Opción " + data + " desconocida, utilice ON,OFF,SWITCH,STATE")
        

GPIO.setmode(GPIO.BOARD)
SimpleWrite()