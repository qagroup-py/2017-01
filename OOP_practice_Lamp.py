class BaseLamp:
    def __init__(self, color, voltage, bulbs):
        """
        color (str): lamp body color
        voltage (int): expected operational voltage
        bulbs (list): list with `Bulb` objects
        """
        self.color = color
        self.voltage = voltage
        self.bulbs = bulbs
        self.turned_on = False

    def current_power(self):
        """Returns current power being consumed by lamp"""
        if self.turned_on:
            return self.max_power()
        else:
            return 0

    def max_power(self):
        """Returns peak power of lamp"""
        total_power = 0
        for bulb in self.bulbs:
            total_power += bulb.power
        return total_power


class DumbLamp(BaseLamp):
    """Lamp with two buttons – to turn on and off separately"""

    def turn_on(self):
        self.turned_on = True

    def turn_off(self):
        self.turned_on = False


class SmartLamp(BaseLamp):
    """Lamp with unified power button – turns on when lamp is off and vice versa"""

    def switch(self):
        self.turned_on = not self.turned_on


class Bulb:
    possible_cartridges = ['E14', 'E27', 'G4']

    def __init__(self, cartridge, power):
        """
        cartridge (str): cartridge type, must be one of `Bulb.possible_cartridges`
        power (int): power consumption of single bulb
        """
        if cartridge in self.possible_cartridges:
            self.cartridge = cartridge
        else:
            raise Exception('invalid cartridge type')
        self.power = power
