# password-validity-program-
# password-validity-program-
import string
digits= string.digits
upp= string.ascii_uppercase
low= string.ascii_lowercase
special_char= string.punctuation
space=' '
flag=1
d={digits:0,upp:0,low:0,special_char:0}
password=input("enter a password")
if len(password)>=8 and len(password)<15:
    for i in password:
        if i in digits:
            d[digits]=1
        elif i in upp:
            d[upp]=1
        elif i in low:
            d[low]=1
        elif i in special_char:
            d[special_char]=1
if space in password:
    flag=0
if 0 not in d.values() and flag==1:
    print("password is valid")
else:
    print("please enter a correct password!!! it is invalid")