import argparse
import datetime

def string_to_datetime(date_string):
    """
    Converts string in format DD-MM-YYYY to a datetime.datetime object.
    """
    date = datetime.datetime.strptime(date_string, "%d-%m-%Y")
    return(date)

def check_valid_input(start_date, end_date):
    """
    Ensures inputs are valid, and converts them to datetime.datetime objects if they are 
    strings.
    """
    start_is_valid_str = False
    end_is_valid_str   = False

    start_type = type(start_date)
    end_type   = type(end_date)
    
    if start_type == str:
        start_date = string_to_datetime(start_date)
        start_is_valid_str = True
    if end_type == str:
        end_date = string_to_datetime(end_date)
        end_is_valid_str = True
    
    if isinstance(start_type, datetime.datetime) or isinstance(start_type, datetime.date):
        pass
    elif start_is_valid_str == False:
        raise TypeError(
            "Start date must be a string, datetime.datetime or datetime.date object."
        )
    
    if end_date == None:
        # Start date is valid, no end date given.
        return(start_date, end_date) 
    elif isinstance(end_type, datetime.datetime) or isinstance(end_type, datetime.date):
        pass
    elif end_is_valid_str == False:
        raise TypeError(
            "When supplied, end date must be a string, datetime.datetime or datetime.date object."
        )
    
    if start_date > end_date:
        raise ValueError("Start date is after end date.")
    elif start_date == end_date:
        raise ValueError("Time interval must be one day or longer.")
    else:
        return(start_date, end_date)

def day_with_suffix(day):
    """
    Adds a suffix to a given int (i.e. 1st, 2nd, 31st) and returns it as a string.
    
    day - 0 < int < 100
    """
    suffix = 'th' if 11<=day<=13 else {1:'st', 2:'nd', 3:'rd'}.get(day%10, 'th')
    return(str(day) + suffix)    

def custom_strftime(format, date):
    """
    Custom implementation of datetime.strftime() to add suffix to the day of the month.
    """
    day = day_with_suffix(date.day)
    return(date.strftime(format).replace('{S}', day))

def friendlify(start_date, end_date=None):
    """
    Returns interval of given dates in a human friendly string. 
    If end_date not given, returns human friendly string of start_date.
    
    Arguments can either be strings or datetime.datetime objects.
    """
    start, end = check_valid_input(start_date, end_date)
    
    if end==None:
        return(custom_strftime('{S} %B, %Y', start))

    if start.year == end.year:
        if start.month == end.month:
            # Same month, same year
            part1 = custom_strftime('{S}', start)
            part2 = custom_strftime('{S} %B, %Y', end)
            return(part1 + " - " + part2)
        
        # Different month, same year
        part1 = custom_strftime('{S} %B', start)
        part2 = custom_strftime('{S} %B, %Y', end)
        return(part1 + " - " + part2)
    
    else:
        # Different month and year
        part1  = custom_strftime('{S} %B, %Y', start)
        part2  = custom_strftime('{S} %B, %Y', end)
        return(part1 + " - " + part2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("start_date", 
                        help="starting date for the time interval in form DD-MM-YYYY",
                        )
    parser.add_argument("end_date", 
                        help="ending date for the time interval in form DD-MM-YYYY",
                        nargs='?',
                        default=None,
                        )
    args= parser.parse_args()
    print(friendlify(args.start_date, args.end_date))

if __name__ == '__main__':
    main()

