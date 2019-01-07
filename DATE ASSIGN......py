print('Muhammad Hamza Adnan - 18B-017-CS - Section A')
print('Checking dates with respect to given formats')
date_format = str(input("Enter date format dd-mm-yy or mm-dd-yy, for dd-mm-yy enter 1 and for mm-dd-yy enter any number : "))
if date_format == '1':
    for char in range(11):
        date = input("Enter the complete date: ")
        dd, mm, yy = date.split('-')
        dd = int(dd)
        mm = int(mm)
        yy = str(yy)
        if (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
            max_days = 31
        elif (mm == 4 or mm == 6 or mm == 9 or mm == 11):
            max_days = 30
        else:
            max_days = 28
        if (mm < 1 or mm > 12):
            print("Date is invalid,error in months.")
        elif (len(yy) > 4):
            print('year is invalid as per the format')
        elif (dd < 1 or dd > max_days):
            print("Date is invalid,you have entered an invalid day .")
        else:
            print('Date is valid.')
else:
    for char in range(11):
        date = input("Enter the complete date : ")
        mm, dd, yy = date.split('-')
        dd = int(dd)
        mm = int(mm)
        yy = str(yy)
        if (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
            max_days = 31
        elif (mm == 4 or mm == 6 or mm == 9 or mm == 11):
            max_days = 30
        else:
            max_days = 28
        if (mm < 1 or mm > 12):
            print("Date is invalid,error in number of months.")
        elif (len(yy) > 4):
            print('year is invalid as per the format')
        elif (dd < 1 or dd > max_days):
            print("Date is invalid,you have entered an invalid day.")
        else:
            print('Date is valid.')
