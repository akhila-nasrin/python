s='Learning python is fun!'
print("length of" , s, "is", len(s))

s='Learning python is fun!'
print(s.lower())

s='Learning python is fun!'
print(s.upper())

s='LEARNing PYTHON is fun!'
print(s.swapcase())

s='Learning python is fun!'
print(s.capitalize())

s='Learning python is fun!'
print(s.title())

s='Learning python is fun!'
print(s.lstrip())
s='*******Learning python is fun!'
print(s.lstrip('*'))

s='Learning python is fun!'
print(s.rstrip())
s='Learning python is fun!*****'
print(s.rstrip('*'))

s='Learning python is fun!'
print(s.strip())
s='******Learning python is fun!*******'
print(s.strip('*'))


s='Learning python is fun!'
print('maximum character is :',max(s))

s='Learning python is-fun!'
print('minimum character is :',min(s))

s="This is very new.This is good"
print(s.replace('is','was'))
print(s.replace('is','was',2))

s="This is python programming"
print(s.center(30, '*'))
print(s.center(30))

s="This is python programming"
print(s.ljust(30, '*'))
print(s.ljust(30))

s="This is python programming"
print(s.rjust(30, '*'))
print(s.rjust(30))

s="This is python programming"
print(s.zfill(30))

s="This is python programming"
print(s.count('i',0,10))
print(s.count('i',0,25))

s="This is python programming"
print(s.find('thon',0,25))
print(s.rfind('thy'))

s="This is python programming"
print(s.index('thon',0,25))
print(s.index('thy'))

s="This is python programming"
print(s.rindex('thon',0,25))
print(s.rindex('thy'))

s="python programming is fun"
print(s.startswith('is',10,21))
s="python programming is fun"
print(s.startswith('is',19,25))

s="python programming is fun"
print(s.endswith('is',10,21))
s="python programming is fun"
print(s.endswith('is',0,25))

s=u"This is python 1234"
print(s.isdecimal())
s=u"123456"
print(s.isdecimal())

s="This is python 1234"
print(s.isalpha())
s="python"
print(s.isalpha())

s="****This is python 1234"
print(s.isalnum())
s="python1234"
print(s.isalnum())

s="****python1234"
print(s.isdigit())
s="123456"
print(s.isdigit())

s="Python Programming"
print(s.islower())
s="python programming"
print(s.islower())

s="Python Programming"
print(s.isupper())
s="PYTHON PROGRAMMING"
print(s.isupper())








