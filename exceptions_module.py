GREETING = 'Hello, '
_GREETING = 'Hello again, '

class BadName(Exception):
    pass

def greet(name):
    if name[0].isupper():
        return GREETING + name
    else:
        raise BadName(name + ' is inappropriate name')

def _private_method():
    print('Private method')

print('Import is execution')

__all__ = ['BadName', 'greet']