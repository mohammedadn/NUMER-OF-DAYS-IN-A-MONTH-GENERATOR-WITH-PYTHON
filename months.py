def num_days(month):

    if month == ('jan, march, may, july, august, oct, dec'):
        print('number of days in',month,'is',31)
    elif month == 'feb':
        print('number of days in',month,'is',28)
    else:
        print('number of days in',month,'is',30)
   

num_days('june')

