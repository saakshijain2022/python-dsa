def is_leap(year): # in bracket for input year is def f (a,b)    a=year
    leap = False
    if year%4==0 and (year%400==0 or year %100 !=0 ):
    # Write your logic here
      leap = True
      
    else:
        leap = False  
        return leap
        
year = int(input())
print( is_leap(year))
