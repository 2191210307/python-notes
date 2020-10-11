# 2-1 简单消息：将一条消息存储到变量中，再将其打印出来。
# 2-2 多条简单消息：将一条消息存储到变量中，将其打印出来；再将变量的值修改为一条新消息，并将其打印出来。

# easy message.py
message = 'You only live once.'
'''
Eat drink and be merry for tomorrow we die.\
Seize the day.\
Life is too short and please enjoy it fully.\
'''
print(message)

message = 'Life is too short and please enjoy it fully.'
print(message)

name = "my sun"
print("Hello " + name + ", would you like to learn some Python today?")
print(name.upper()) 
print(name.lower())
print(name.title())

famous_person = "王阳明" 
message = "破山中贼易 破心中贼难"
print(famous_person + "once said, "  "“" + message + ".”")

name = " \tAB C\n  "
print(name)
print(name.strip())
print(name.lstrip())
print(name.rstrip())
