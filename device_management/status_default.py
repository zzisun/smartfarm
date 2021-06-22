class Status_Default():
    humid_level = [{'min': 50}, {'max' : 70}, {'avg' : 60}]
    temp = [{'min':55}, {'max':70}, {'avg':65}]
    co2 = [{'min' : 400}, {'max':410}]
    oxygen = [{'min':5}, {'max':8}]


    def chk_humid(self, humid):
        if humid < self.humid_level['min']:
            return -1
        elif humid > self.humid_level['max']:
            return 1
        return 0
    
    def chk_temp(self, temp):
        if temp < self.temp_level['min']:
            return -1
        elif temp > self.temp_level['max']:
            return 1
        return 0

    def chk_co2(self, co2):
        if co2 < self.co2_level['min']:
            return -1
        elif co2 > self.co2_level['max']:
            return 1
        return 0
        
    def chk_oxygen(self, oxygen):
        if oxygen < self.oxygen_level['min']:
            return -1
        elif oxygen > self.oxygen_level['max']:
            return 1
        return 0           