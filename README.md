# friendly_dates
A simple python module for displaying date intervals and dates in a simple 
and human friendly format. 

## Usage
The dates of the interval to be 'friendlified' must either be strings in 
the form "D-M-YYYY", or python datetime.datetime objects. They can be a 
mixture of both (e.g. the starting date is a string, ending date is a 
datetime.datetime object).

Importing:

    >>> from friendly_dates import friendlify

Interval spanning different years: 

    >>> friendlify("6-5-2012", "06-05-2020")
    '6th May, 2012 - 9th September, 2020'
  
Interval spanning different months:

    >>> friendlify("6-5-2012", "6-7-2012")
    '6th May - 6th July, 2012'

Interval spanning same month:

    >>> friendlify("06-05-2012", "12-05-2012")
    '6th - 12th May, 2012'

Friendlifying a single date:

    >>> friendlify("01-01-1900") # This is the earliest supported date
    '1st January, 1900' 

Passing datetime.datetime objects as arguments:

    >>> date1 = datetime.datetime.now()
    >>> date2 = date1 + datetime.timedelta(days=365)
    >>> date1
    datetime.datetime(2015, 4, 13, 20, 27, 7, 742641)
    >>> date2
    datetime.datetime(2016, 4, 12, 20, 27, 7, 742641)
    >>> friendlify(date1, date2)
    '13th April, 2015 - 12th April, 2016'

Using the module from the command line:

    chrsintyre@samson:~/friendly_dates$ python friendly_dates.py 12-12-2012 14-12-2012
    12th - 14th December, 2012
    chrsintyre@samson:~/friendly_dates$ python friendly_dates.py 12-12-2099
    12th December 2099
