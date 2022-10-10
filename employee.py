"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from unicodedata import name


class Employee:
    def _init_(self, name, contract, salaryCal , hours, isCommission , commissionType , commission , contractsNum ):
        self.name = name
        self.contract = contract
        self.salaryCal = salaryCal
        self.hours = hours
        self.isCommission = isCommission
        self.commissionType = commissionType
        self.commission = commission
        self.contractsNum = contractsNum
        

    def get_pay(self):
        totalPay = 0

        if self.contract == "monthly":
            if self.isCommission == False:
                totalPay = self.salaryCal

            elif self.isCommission and self.commissionType == "bonus":
                totalPay = self.salaryCal + self.commission

            else:
                totalPay = self.salaryCal +  (self.contractsNum * self.commission)

        elif self.contract == "hourly":
            if self.isCommission == False:
                totalPay = self.salaryCal * self.hours

            elif self.isCommission and self.commissionType == "bonus":
                totalPay = (self.salaryCal * self.hours) + self.commission

            else:
                totalPay = (self.salaryCal * self.hours) +  (self.contractsNum * self.commission)

        return totalPay






    def _str_(self):
        empString = ""
        
        if self.contract == "monthly":
            if self.isCommission == False:
                empString += f'{self.name} works on a monthly salary of {self.salaryCal}.  Their total pay is {self.get_pay()}.'

            elif self.isCommission and self.commissionType == "bonus":
                empString += f'{self.name} works on a monthly salary of {self.salaryCal} and receives a bonus commission of {self.commission}.  Their total pay is {self.get_pay()}.'

            else:
                empString += f'{self.name} works on a monthly salary of {self.salaryCal} and receives a commission for {self.contractsNum} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}.'


        elif self.contract == "hourly":
            if self.isCommission == False:
                empString += f'{self.name} works on a contract of {self.salaryCal} hours at {self.hours}/hour.  Their total pay is {self.get_pay()}.'

            elif self.isCommission and self.commissionType == "bonus":
                empString += f'{self.name} works on a contract of {self.salaryCal} hours at {self.hours}/hour and receives a bonus commission of {self.commission}.  Their total pay is {self.get_pay()}.'

            else:
               empString += f'{self.name} works on a contract of {self.salaryCal} hours at {self.hours}/hour and receives a commission for {self.contractsNum} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}.'                
        
        return empString


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly", 4000, 0, False, "None", 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', 100, 25, False, "None", 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'monthly', 3000, 0, True, 'contract', 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly', 150, 25, True, "contract", 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'monthly', 2000, 0, True, "bonus", 1500,0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', 120, 30, True, "bonus", 600, 0)