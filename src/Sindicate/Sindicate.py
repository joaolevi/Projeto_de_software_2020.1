class Sindicate:
    def __init__(self, taxPerMonth):
        self.__taxPerMonth = taxPerMonth
        self.__serviceTax = {'Medical':32.45,'Lawyer':45.34, 'indemnity':25.16}
    
    def get_taxPerMonth(self):
        return self.__taxPerMonth
    def set_taxPerMonth(self, new_taxPerMonth):
        self.__taxPerMonth = new_taxPerMonth
    
    def get_serviceTax(self, tax_type):
        return self.__serviceTax[tax_type]
    def set_serviceTax(self, new_serviceTax, value):
        self.__serviceTax[new_serviceTax] = value

    def id_generetor(self, emp):
        new_id = int(emp.rg[:-4])*17
        emp.sind_id = new_id

    def month_tax_roll(self, members):
        for m in members:
            if m.sindMember:
                m.tax_value += self.__taxPerMonth

    def tax_associator(self, emp, tax_value):
        emp.tax_value += tax_value