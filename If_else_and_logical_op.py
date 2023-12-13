year=int(input("Enter year : "))
if(year%4==0):
    if(year%4==0 and year%100!=0):
        print(f"The given year {year} is a leap Year..")
    elif(year%100==0 and year%400==0):
        print(f"The given year {year} is a leap Year..")
else:
    print(f"The given year {year} is not a leap Year..")
indfind