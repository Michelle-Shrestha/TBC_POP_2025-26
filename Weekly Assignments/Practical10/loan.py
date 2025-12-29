class Loan:
    def __init__(self,annualInterestRate=2.5, numberOfYears=1, loanAmount=1000):
        self.__annualInterestRate = annualInterestRate
        self.__numberOfYears = numberOfYears
        self.__loanAmount = loanAmount

        if self.__annualInterestRate<=0:
            raise ValueError ("Invalid Annual Interest Rate")
        if self.__numberOfYears<=0:
            raise ValueError ("Invalid number of years")
        if self.__loanAmount<=0:
            raise ValueError ("Invalid Loan Amount")


    #Setters
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def setNumberOfYears(self, numberOfYears):
        self.__numberOfYears = numberOfYears
    
    def setLoanAmount(self, loanAmount):
        self.__loanAmount = loanAmount

    #getters
    def getAnnualInterestRate(self):
        if self.__annualInterestRate<=0:
            raise ValueError ("Invalid Annual Interest Rate")
        return self.__annualInterestRate
    
    def getNumberOfYears(self):
        if self.__numberOfYears<=0:
            raise ValueError ("Invalid number of years")
        return self.__numberOfYears
    
    def getLoanAmount(self):
        if self.__loanAmount<=0:
            raise ValueError ("Invalid Loan Amount")
        return self.__loanAmount
    
    def getMonthlyPayment(self):
        monthlyInterestRate = self.__annualInterestRate / 1200
        numberOfPayments = self.__numberOfYears*12
        # " \ " is a continuation character which tells python statement continues on next line
        monthlyPayment= self.__loanAmount * monthlyInterestRate * (1 + monthlyInterestRate)* numberOfPayments \
        / ((1+monthlyInterestRate)*numberOfPayments)

        return monthlyPayment
    
    def getTotalPayment(self):
        totalPayment= self.getMonthlyPayment() * self.__numberOfYears* 12
        return totalPayment

try:   
    l = Loan(7.5,30,100000)
    print("Total payment: "+ str(l.getTotalPayment()))

    m= Loan(-1,3,3)
    print("Total payment: "+ str(m.getTotalPayment()))

except ValueError as e:
    print(e)