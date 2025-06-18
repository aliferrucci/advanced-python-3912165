# Example file for Advanced Python by Joe Marini
# Programming challenge for working with Exceptions

# Implement the InvalidTempError exception class here
class InvalidTempError(Exception):
    """Raise exception when temperature is out of range below 100 or above 500 degrees"""
    def __init__(self, temp):
        message = f"Invalid temperature setting: {temp}. Must be between 100 and 500 degrees or zero"
        super().__init__(message)

class DigitalOven:
    def __init__(self):
        self.temp = 0

    def set_temp(self, temp):
        if 0 < temp < 100 or temp > 500:
            raise InvalidTempError(temp)
        self.temp = temp

    def get_temp(self):
        return self.temp

def test_oven(test_temp):
    global oven
    try:
        oven.set_temp(test_temp)
    except InvalidTempError as e:
        print(f"Error: {e}")
    else:
        print(f"Temperature was set to {test_temp} degrees")
    finally:
        print(f"Current temp setting is {oven.get_temp()}")

# An "InvalidTempError" Exception should be raised if the temperature
# is set below 100 degrees or above 500 degrees
oven = DigitalOven()
test_oven(250)
test_oven(50)
test_oven(0)
test_oven(600)
