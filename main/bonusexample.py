password = input("enter password: ")
result ={}
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["uppercase"] = uppercase

if all(result.values()) :
    print("strong password ")
else:
    print("weak password")


