#  "in" Operator:

# in ka matlab hota hai membership check karna.. yani koi value kisi list, string, ya or kisi collection ke andar hai ya nahi..

list = [1, 2, 3]

print(2 in list)  # True.. 2 list mai hai..
print(4 in list)  # False.. 4 list mai nahi hai..




# "is" Operator:

# is ka istemal identity check karne ke liye hota hai.. yani do chezein memory mein ek hi jagah par hen ya nahi..

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True.. dono ek hi list hen
print(a is c)  # False.. value same hai lekin object alag hai
