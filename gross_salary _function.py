def basic_salary(basics):
  TA=0.1*basics
  DA=0.12*basics
  gross_salary=basics+TA+DA
  print(gross_salary)
basics=int(input("enter the basic salary"))
print(basic_salary(basics))