import argparse
import datetime

def string_to_datetime(date_string):
    """
    Converts string in format DD-MM-YYYY to a datetime.datetime object.
    """
    date = datetime.datetime.strptime(date_string, "%d-%m-%Y")
    return(date)

def check_interval(start_date, end_date):
    """
    Checks two datetime objects against eachother to make sure
        1) The first date isn't after the second date
        2) They are not the same day
    """
    if start_date > end_date:
        raise ValueError("Start date is after end date.")
    elif start_date == end_date:
        raise ValueError("Time interval must be one day or longer.")

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


def friendlify(start_date, end_date):
    """
    Returns interval of given dates in a human friendly format.

    input: two dates either as strings in DD-MM-YYYY format, 
           or as a datetime.datetime objects.
    ouput: string
    """
    
    if type(start_date) == str:
        start_date = string_to_datetime(start_date)
    if type(end_date) == str:
        end_date = string_to_datetime(end_date)

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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("start_date", 
                        help="starting date for the time interval in form DD-MM-YYYY"
                        )
    parser.add_argument("end_date", 
                        help="ending date for the time interval in form DD-MM-YYYY"
                        )
    args= parser.parse_args()
    print(friendlify(args.start_date, args.end_date))

if __name__ == '__main__':
    main()

