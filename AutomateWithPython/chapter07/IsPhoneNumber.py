import re

phoneNum = 'My number is 415-555-4242.'
print(phoneNum)

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneNumRegex.search(phoneNum)
print('Phone number found: ' + mo.group())

phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phoneNumRegex.search(phoneNum)
print('Phone number found group(1): ' + mo.group(1))
print('Phone number found group(2): ' + mo.group(2))
print('Phone number found group(0): ' + mo.group(0))
print('Phone number found group(): ' + mo.group())

areaCode, mainNumber = mo.groups()
print("areaCode:", areaCode)
print("mainNumber:", mainNumber)
