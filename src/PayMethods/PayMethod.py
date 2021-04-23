class PayMethod():
    def __init__(self, value, date):
        self.value = value
        self.date = date

    def get_value(self):
        return self.value
    def set_value(self, new_value):
        self.value = new_value
    
    def get_date(self):
        return self.date
    def set_date(self, new_date):
        self.date = new_date

    def __repr__(self):
        return "%.2f, %s" %(self.value, self.date)