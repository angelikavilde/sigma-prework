
from datetime import datetime

def age(given_date):
      current_date = datetime.now()
      given_date = datetime.strptime(given_date, "%d-%m-%Y")
      
      year = (current_date.year)-(given_date.year)
      
      if year == 0:
            return year
      
      if (current_date.month)<(given_date.month):
            return year-1
      
      elif (current_date.month)==(given_date.month):
            if (current_date.day)<(given_date.day):
                  return year-1
            else:
                  return year
      else:
            return year
