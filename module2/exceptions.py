# try:
#     x = [1, 2, 'hello', 7]
#     x.sort()
#     print(x)
# except TypeError:
#     print('Type error')
#
# print('End')

# def f(x, y):
#     try:
#         return x / y
    # except TypeError:
    #     print('Type error')
    # except ZeroDivisionError:
    #     print('Zero division')
    # except (TypeError, ZeroDivisionError):
    #     print('Error')
    # except (TypeError, ZeroDivisionError) as e:
    #     print(type(e))
    #     print(e)
    #     print(e.args)
    # except:
    #     print('Error')

# print(f(5, 0))
# print(f(5, []))

# try:
#     15 / 0 # e
# except ZeroDivisionError: # isinstance(e, ZeroDivisionError) == True
#     print('Divizion by zero')
# except ArithmeticError:  # isinstance(e, ArithmeticError) == True
#     print('Arithmetic Error')


# print(ZeroDivisionError.mro())

# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print('division by zero')
#     else:
#         print('result is', result)
#     finally:
#         print('finally')
#
# divide(2, 1)
# divide(2, 0)
# divide(2, [])

def greet(name):
    if name[0].isupper():
        return 'Hello, ' + name
    else:
        raise ValueError(name + ' is inappropriate name')

# print(greet('Anton'))
# print(greet('anton'))

while True:
    try:
        name = input('Please enter youe name: ')
        greeting = greet(name)
        print(greeting)
    except ValueError:
        print('Please try again')
    else:
        break

class BadName(Exception):
    pass

def greet(name):
    if name[0].isupper():
        return 'Hello, ' + name
    else:
        raise BadName(name + ' is inappropriate name')

print(greet('Anton'))
print(greet('anton'))