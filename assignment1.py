"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""

initial = int(input("enter initial investment:  "))
annual = int(input("enter annual interest rate:  "))
time = int(input("enter time limit:   "))

a = annual / 100
print(a)
while True:
  timevalue = input("enter length of time  1 for year, 2 for month, 3 for day:  ")

  if timevalue == "1":
    break
  elif timevalue == "2":
    time /= 12
    break
  elif timevalue == "3":
    time/365
    break
  else:
    print("re-enter the length of time")

I = initial * a * time
print(f"the amount of money you have earned is  ${I}")