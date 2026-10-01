class PCA9555:
    INPUT0=0x00
    OUTPUT0=0x02
    POLARITY0=0x04
    CONFIG0=0x06

    def __init__(self, i2c, address=0x20):
        self.i2c=i2c
        self.address=address
        self._write16(self.CONFIG0,0xFFFF)
        self._write16(self.POLARITY0,0x0000)
        self._write16(self.OUTPUT0,0x0000)

    def _write16(self, reg, value):
        while not self.i2c.try_lock():
            pass
        try:
            self.i2c.writeto(self.address, bytes((reg,value&255,(value>>8)&255)))
        finally:
            self.i2c.unlock()

    def _read16(self, reg):
        b=bytearray(2)
        while not self.i2c.try_lock():
            pass
        try:
            self.i2c.writeto_then_readfrom(self.address,bytes((reg,)),b)
        finally:
            self.i2c.unlock()
        return b[0] | (b[1]<<8)

    def configure_input(self,pin):
        cfg=self._read16(self.CONFIG0)
        self._write16(self.CONFIG0,cfg | (1<<pin))

    def configure_output(self,pin,value=False):
        cfg=self._read16(self.CONFIG0)
        self._write16(self.CONFIG0,cfg & ~(1<<pin))
        self.value(pin,value)

    def value(self,pin,new_value=None):
        if new_value is None:
            return bool(self._read16(self.INPUT0)&(1<<pin))
        out=self._read16(self.OUTPUT0)
        if new_value: out |= 1<<pin
        else: out &= ~(1<<pin)
        self._write16(self.OUTPUT0,out)

class PCA9555Pin:
    def __init__(self,expander,pin):
        self.expander=expander
        self.pin=pin
    def switch_to_input(self,pull=None):
        self.expander.configure_input(self.pin)
    def switch_to_output(self,value=False):
        self.expander.configure_output(self.pin,value)
    @property
    def value(self):
        return self.expander.value(self.pin)
    @value.setter
    def value(self,v):
        self.expander.value(self.pin,v)
