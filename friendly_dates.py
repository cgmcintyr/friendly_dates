import argparse
import datetime

def string_to_datetime(date_string):
    """
    Converts string in format DD-MM-YYYY to a datetime.datetime object.
    """
    try:
        date = datetime.datetime.strptime(date_string, "%d-%m-%Y")
        return(date)
    except ValueError:
        print("ValueError: '{0}' is not a valid 'dd-mm-yyyy' date.".format(date_string))
        quit()

def check_interval(start_date, end_date):
    """
    Checks two datetime objects against eachother to make sure
        1) The first date isn't after the second date
        2) They are not the same day
    """
    if start_date > end_date:
        print("Error: start date is after end date.")
        quit()
    elif start_date == end_date:
        print("Error: time interval must be one day or longer.")
        quit()

def day_with_suffix(day):
    """
    Adds a suffix to a given int (i.e. 1st, 2nd, 31st) and returns it as a string.
    
    day - 0 < int < 100
    """
    suffix = 'th' if 11<=day<=13 else {1:'st', 2:'nd', 3:'rd'}.get(day%10, 'th')
    return(str(day) + suffix)    

def custom_strftime(format, date):
    day = day_with_suffix(date.day)
    return(date.strftime(format).replace('{S}', day))


def friendlify(start_date, end_date):
    """
    Returns interval of given dates in a human friendly format.

    input: datetime.datetime or datetime.date objects
    ouput: string
    """
    check_interval(start_date, end_date)

    if start_date.year == end_date.year:
        if start_date.month == end_date.month:
            # Same month, same year
            part1 = custom_strftime('{S}', start_date)
            part2 = custom_strftime('{S} %B, %Y', end_date)
            return(part1 + " - " + part2)
        
        # Different month, same year
        part1 = custom_strftime('{S} %B', start_date)
        part2 = custom_strftime('{S} %B, %Y', end_date)
        return(part1 + " - " + part2)
    
    else:
        # Different month and year
        part1  = custom_strftime('{S} %B, %Y', start_date)
        part2  = custom_strftime('{S} %B, %Y', end_date)
        return(part1 + " - " + part2)

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("start_date", 
                        help="starting date for the time interval in form DD-MM-YYYY"
                        )
    parser.add_argument("end_date", 
                        help="ending date for the time interval in form DD-MM-YYYY"
                        )
    args= parser.parse_args()

    date1 = string_to_datetime(args.start_date)
    date2 = string_to_datetime(args.end_date)

    print(dateify(date1, date2))

    

if __name__ == '__main__':
    Main()


