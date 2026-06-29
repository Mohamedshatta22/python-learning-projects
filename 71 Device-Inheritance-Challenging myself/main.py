class electric_machine():
    def __init__(self):
        self.power = "electricity"
        self.restatr_function = True
        self.device_is_working_now = True
        self.name = "device"
    def opening_the_machine(self):
        self.device_is_on = f"the {self.name} is open right now"
        return self.device_is_on
    def closing_the_machine(self):
        self.device_is_off = f"the {self.name} is off right now"
        self.device_is_working_now = False
        return self.device_is_off
    def restart_request(self):
        qu = input(f"do you want to make restart {self.name} ").lower()
        return qu 
    def making_process(self):
        if self.restart_request()=="no":
            x = self.opening_the_machine()
            print(x)
            print(f"the status of the {self.name} right now is {self.device_is_working_now}")
        else:
            y = self.closing_the_machine()
            print(y)
            print(f"the status of the {self.name} right now is {self.device_is_working_now}")
class laptop(electric_machine):
    def __init__(self):
        super().__init__()
        self.name = "laptop"
    def opening_the_machine(self):
        return super().opening_the_machine()
    def closing_the_machine(self):
        return super().closing_the_machine()
    def restart_request(self):
        return super().restart_request()
    def making_process(self):
        return super().making_process()
      

device1 = laptop()
device1.making_process()
