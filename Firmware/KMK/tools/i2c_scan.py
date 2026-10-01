import board,busio

def scan(name,scl,sda):
    i2c=busio.I2C(getattr(board,"GP"+str(scl)),getattr(board,"GP"+str(sda)),frequency=100000)
    while not i2c.try_lock():
        pass
    try:
        print(name, [hex(x) for x in i2c.scan()])
    finally:
        i2c.unlock()

scan("SCL/SDA",7,6)
scan("SCL1/SDA1",21,20)
