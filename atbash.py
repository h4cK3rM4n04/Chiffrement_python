#coding:utf-8
import string as s

x = s.ascii_letters+' '+s.punctuation
y = x[::-1]

word = ']4|W3/U4=04'
transformation = str.maketrans(x, y)
result = str.translate(word, transformation)

print(result)