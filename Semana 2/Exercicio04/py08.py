def hello_func():
    pass 

print(hello_func())

def hello_func():
    print('Hello function!')

hello_func()

def hello_func():
    return 'Hello function!!'

print(hello_func())

print(hello_func().upper())

def hello_func(greeting):
    return '{} function!!'.format(greeting)

print(hello_func('Hi'))

def hello_func(greeting, name = 'You'):
    return '{}, {}!!'.format(greeting, name)

print(hello_func('Hi'))

def hello_func(greeting, name = 'You'):
    return '{}, {}!!'.format(greeting, name)

print(hello_func('Hi', name = 'Corey'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name = 'John', age=22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year):
    """Return True for leap years, False for non-leap years.""" 
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(is_leap(2017))
print(days_in_month(2017, 2))
