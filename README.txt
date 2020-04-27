pydate

A Python package made to format date & time strings for use in various SQL RDBMS.

Make sure to have the latest version of Python 3 installed although this should work with previous versions. 
Pip and git also need to be installed for package installation with command line.  

To install/update the package with pip enter command in terminal:
    pip install git+https://github.com/CodeConfidant/pydate-time.git#egg=pydate-time

To uninstall the package with pip enter command in terminal:
    pip uninstall pydate

-----------
Module Year
-----------
Attribute/Method 	        Description
year 	                    Attribute of the int type representing a year.
                            The attribute must be 4 digits.

get_year() 	                Return the year attribute value.

set_year(year) 	            Change the year attribute value.

tostring() 	                Return a string representing the Year class attribute values. 

-----------
Module Date
-----------
Note: This class inherits the attributes/methods of the Year class. 

Attribute/Method 	        Description
month 	                    Attribute of the int type representing a month.
                            The attribute's value must be between 1 & 12.

day 	                    Attribute of the int type representing a day.
                            The attribute's value must be between 1 & 31.

get_month() 	            Return the month attribute value.

get_day() 	                Return the day attribute value.

set_month(month) 	        Change the month attribute value.

set_day(day) 	            Change the day attribute value.

tostring() 	                Return a string representing the Date class attribute values.

-----------
Module Time
-----------
Attribute/Method 	        Description
hour 	                    Attribute of the int type representing a hour.
                            The attribute's value must be between 0 & 23.

minute 	                    Attribute of the int type representing a minute.
                            The attribute's value must be between 0 & 59.

second 	                    Attribute of the int type representing a second.
                            The attribute's value must be between 0 & 59.

get_hour() 	                Return the hour attribute value.

get_minute() 	            Return the minute attribute value.

get_second() 	            Return the second attribute value.

set_hour(hour) 	            Change the hour attribute value.

set_minute(minute) 	        Change the minute attribute value.

set_second(second) 	        Change the second attribute value.

tostring() 	                Return a string representing the Time class attribute values.

---------------
Module DateTime
---------------
Note: This class inherits the attributes/methods of both the Date & Time classes.

Method 	                    Description
tostring() 	                Return a string representing the DateTime class attribute values. 