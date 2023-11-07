import datetime
def school_year():
    month = int(str(datetime.datetime.now())[5:7])
    if month >= 9:
        return str(datetime.datetime.now())[0:4] + '-' + str(int(str(datetime.datetime.now())[0:4]) + 1)
    else:
        return str(int(str(datetime.datetime.now())[0:4]) - 1) + '-' + str(datetime.datetime.now())[0:4]