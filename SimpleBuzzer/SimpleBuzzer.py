import habcatev,time
import re 
import RPi.GPIO as GPIO


class SimpleBuzzer(habcatev.device.Device.Device):
    def __init__(self):
        super(SimpleBuzzer, self).__init__()

    def init(self):
        self.log.logger.error("Iniciando ...")
        self.setSubscriptionArr([self.config['topics']['input']])
        self.pin = self.config['pin']
        self.sequence = self.config['sequence'].split(',')
        self.state = self.config['initialState'].upper()
        GPIO.setup(self.pin, GPIO.OUT)
       
    def playSequence(self):
        for el in self.sequence:
            thi = el.strip()
            if re.match(r"^(s\d+|z\d+)$", thi):
                if re.match(r"s\d", thi):
                    tim=int(re.search(r'(s)(\d)', thi, re.IGNORECASE).group(2))
                    self.log.logger.debug("beep " + str(tim) + "s")
                    GPIO.output(self.pin, True)
                    time.sleep(tim)
                elif re.match(r"z\d", thi):
                    tim=int(re.search('(z)(\d)', thi, re.IGNORECASE).group(2))
                    self.log.logger.debug("zzz " + str(tim) + "s")
                    GPIO.output(self.pin, False)
                    time.sleep(tim)
            else:
                self.log.logger.error("Secuencia " + str(thi) + "no valida")


    def on_event(self,topic,data):
        if data.upper() == 'BEEP':
            self.log.logger.info("BEEP")
            self.state='BEEP'
        elif data.upper() == 'STOP':
            self.log.logger.info("STOP")
            self.state='STOP'
            GPIO.output(self.pin, False)
        elif data.upper() == 'LOOP':
            self.log.logger.info("LOOP")
            self.state='LOOP'
        else:
            self.log.logger.error("Opción " + data + " desconocida, utilice START,STOP,LOOP")
        
    def loop(self):
        if self.state == 'LOOP':
            self.playSequence()
        elif self.state == 'BEEP':
            self.playSequence()
            self.state='STOP'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
SimpleBuzzer()