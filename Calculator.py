class Calculator:
    def __init__(self,n1,n2,n3):
        num1=n1
        num2=n2
        num3=n3

    def Add(self):
        sum=num1+num2+num3

    def Multi(self):
        multi=num1*num2*num3

    def Divide(self):
        div=num1/num2
        div1=div/num3
    def Sub(self):
        subt=num1-num2-num3

Cal=Calculator(1,2,3)
Cal.Add()
Cal.Sub()
Cal.Multi()
Cal.Divide()
