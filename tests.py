import friendly_dates

OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'

def info(msg):
    print OKGREEN + msg + ENDC

def err(msg):
    print FAIL + msg +ENDC

def run_test(date_string1, date_string2):
    date1 = friendly_dates.string_to_datetime(date_string1)    
    date2 = friendly_dates.string_to_datetime(date_string2)    
    
    print("        date1 - {0}".format(date1))
    print("        date2 - {0}".format(date2))
    return(friendly_dates.friendlify(date1, date2))

test_list = [
    (('01-07-2015', '04-07-2015'), '1st - 4th July, 2015'),
    (('01-12-2015', '03-02-2016'), '1st December, 2015 - 3rd February, 2016') ,
    (('01-03-2016', '03-05-2016'), '1st March - 3rd May, 2016'),
    (('01-01-2017', '03-01-2017'), '1st - 3rd January, 2017'),
    (('05-09-2022', '03-09-2023'), '5th September, 2022 - 3rd September, 2023'),
    ]

print("---- RUNNING FRIENDLY_DATES TESTS ----")

i = 0
success = 0

for test in test_list:
    i += 1
    print("Test {0}:".format(i))
    print("    input - '{0} {1}'".format(test[0][0], test[0][1]))
    print("    expected ouput - '{0}'".format(test[1]))
    print("    running test...")
    
    tested = run_test(test[0][0], test[0][1])

    if  tested == test[1]:
        info("    SUCCESS")
        info("    Actual output - {0}".format(tested))
        success += 1
    else:
        err("    FAIL")
        err("    Actual ouput - {0}".format(tested))
    print("    ------------------------------    ")

info("TESTS COMPLETE")
info("{0}/{1} successful".format(success, len(test_list)))

