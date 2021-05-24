class PayMethod():
    def __init__(self, name, value, date):
        self.name = name
        self.value = value
        self.date = date

    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name

    def get_value(self):
        return self.value
    def set_value(self, new_value):
        self.value = new_value
    
    def get_date(self):
        return self.date
    def set_date(self, new_date):
        self.date = new_date

    def __repr__(self):
        return "%s: R$ %.2f, %s" %(self.name, float(self.value), self.date)