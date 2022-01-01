import re

batRegex = re.compile(r"Bat(wo)*man")
mo1 = batRegex.search("The Adventures of Batman")
print(mo1.group())

batRegex = re.compile(r"Bat(wo)*man")
mo1 = batRegex.search("The Adventures of Batwoman")
print(mo1.group())

batRegex = re.compile(r"Bat(wo)*man")
mo1 = batRegex.search("The Adventures of Batwowowowoman")
print(mo1.group())
