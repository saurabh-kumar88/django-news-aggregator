import re
from datetime import datetime, date
import math

class Get_DateTime:
	""" 
    This class handels cleaning of publication datetime strings .
    ...

    Methods
    -------
    __init__()
        Holds nothing, reserved for future use

    String_to_datetime()
        First cleans datatime string and then convert string to datetime object
    Get_Time_Diff()
        Calculates time difference between news post time to current datetime    
    """
	
	def __init__(self):
		pass

	def String_to_datetime(self, datetime_String, datetime_format ):
		
		""" Cleans news publications datetime string and convert it in datetime object.

        Parameters
        ----------
        datetime_String : str
            news Publication datetime string
        datetime_format : str
            format of datetime string
        
        Return value
        ------------
        datetime_obj : datetime object
		python's datetime object

        """
		self.datetime_String = datetime_String
		self.datetime_format = datetime_format
		
		
		datetime_String2 = datetime_String.split(" ")
		# Formats of month names found commonly in datetime strings
		patterns = [
		'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
		'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL','AUG', 'SEP', 'OCT', 'NOV', 'DEC',
		'JANUARY', 'FEBRUARY','MARCH','APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER', 
		'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December',
		]
	
		# Slice datetime string from month name to the end, if found
		# e.g if string = "Updated : March 10 2020 10:19 am IST" then 
		# newString = "March 10 2020 10:19 am IST" 
		
		newString = ""
		__match = False # Check is month name present
		for x in range( len(datetime_String2) ):
			for m in patterns:
				sub = re.search( m, datetime_String2[x] )
				if sub :
					__match = True
					for n in datetime_String2[ x : len(datetime_String2) ]:
						newString += str(n) + " " 
					break
				else:
					continue

		if __match is False: # if month name not present e.g 13/02/2020 
			newString = datetime_String 
					 
		if ',' in newString:
			modified_string = newString.replace(",","")	
		else:
			modified_string = newString

		# Removing space from start and ends if present
		modified_string = modified_string.strip() 
		datetime_obj = datetime.strptime( modified_string, datetime_format )
		#return(modified_string)
		return datetime_obj

	def Get_Time_Diff(self, publication_date):
		""" This method calculates the time difference between publication date stored in
		database vs current datetime.

        Parameters
        ----------
        publication_date : str
            news Publication datetime string
    
        Return value
        ------------
        string : str
		a string representing how older or newer a string is

        """
		self.publication_date = publication_date

		now = datetime.now()
		today = now.strftime('%Y-%m-%d %H:%M:%S')

		today = datetime.strptime(today, '%Y-%m-%d %H:%M:%S')
		timeDelta = (today  - publication_date)

		if timeDelta.days == 0:
			if int(timeDelta.seconds) < 60: # Case 1: diff > 1 minute
				return (str(int(timeDelta.seconds)) + " seconds ago")
			elif int(timeDelta.seconds) > 60 and int(timeDelta.seconds) < 3600: # Case 2: diff is between 1 to 59 minutes i.e within a hour
				result = int( int(timeDelta.seconds)/ 60 )
				return ( str(int(result)) + " minutes ago")				
			elif int(timeDelta.seconds) >= 3600: # case 3 : diff is in between 1 to 23 hours
				result = round( (int(timeDelta.seconds)/3600 ), 2)
				# Note: math.modf(realNumber) --------> ('decimal part, integer part') 
				#e.g: math.modf(3.74) return a tuple = (0.7400000000000002, 3.0)
				hr_min = list(math.modf(result))
				hours =  int(hr_min[1]) # Seperating hours
				minutes = int( round(hr_min[0], 2) * 100 ) # Seperating minutes 
				#print("\n hr : ", hr )
				#print("\n min ", minute)
				if minutes >= 60 :
					hours = hours + 1
					minutes = minutes - 60
				return( str(hours) + " hours & " + str(minutes) + " minutes ago") 				  
		else:
			return (str(timeDelta.days) + " days ago")





