# import exceptions_module
# print(exceptions_module.greet('Student'))

# import fib
# print(fib.fib(5))

# import sys
# print(type(sys.modules))
# print(sys.modules)

# import check
# print(sys.modules)
# print(id(check))

# from exceptions_module import BadName, greet
# print(BadName)
# print(greet)

# # import exceptions_module as exc
# from exceptions_module import BadName as bad, greet as exc_greet
# print(bad)
# def greet():
#     print('Greetings')
#
# greet()
# print(exc_greet('Student'))

# from exceptions_module import *
# print(BadName)
# print(greet('Student'))
# # print(GREETING) # ERROR, not in __all__
# # print(_GREETING) # ERROR start with '_', can't access with 'import *'
# # print(_private_method) # ERROR start with '_', can't access with 'import *'