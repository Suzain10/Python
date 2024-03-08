class Employee:
  #Company_Name = "Apple"
  def __init__(self,name):
    self.name = name
    self.raiseAmt = 0.5
    Employee.Company_Name = "Apple"
    self.TotalEmployees +=1

  def showDetails(self):
    print(f"The name of employee is {self.name} and the raise amt is {self.raiseAmt} in { self.TotalEmployees} in {self.Company_Name}")
emp1 = Employee("Harry")
emp1.showDetails()
#Employee.Company_Name ="Meta"



emp2 = Employee("Tom")
emp2.raiseAmt = 10
emp2.Company_Name = "Google"
emp2.showDetails()