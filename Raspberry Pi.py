import RP1.GPI0 as I0
import time
I0.setmode(I0.BOARD)
I0.setup(11,I0.OUT)
while (1):
        I0.output(11,I0.HIGH) # hoac la I0.output(11,1)
        time.sleep(1.0)
        I0.output(11,I0.LOW) # hoac la I0.output(11,0)
        time.sleep(0.5)

