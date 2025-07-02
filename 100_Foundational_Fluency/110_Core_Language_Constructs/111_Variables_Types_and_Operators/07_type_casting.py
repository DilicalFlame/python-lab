"""
demonstrates type casting
"""

# Implicit type casting
a = 5
b = 2.5
c = a + b  # int + float -> float
print("Implicit type casting result:", c)  # Output: 7.5

# Explicit type casting
d = 10
e = 3
f = d / e  # int / int -> float
print("Explicit type casting result:", f)  # Output: 3.3333333333333335

# Converting float to int
g = int(f)  # float to int
print("Converted float to int:", g)  # Output: 3

# Converting string to int
h = "42"
i = int(h)  # string to int
print("Converted string to int:", i)  # Output: 42

# Converting int to string
j = str(d)  # int to string
print("Converted int to string:", j)  # Output: "10"

# Converting float to string
k = str(f)  # float to string
print("Converted float to string:", k)  # Output: "3.3333333333333335"

# Converting string to float
l = "3.14"
m = float(l)  # string to float
print("Converted string to float:", m)  # Output: 3.14

# Converting int to float
n = float(d)  # int to float
print("Converted int to float:", n)  # Output: 10.0

# Converting boolean to int
o = True
p = int(o)  # boolean to int
print("Converted boolean to int:", p)  # Output: 1

# Converting boolean to string
q = str(o)  # boolean to string
print("Converted boolean to string:", q)  # Output: "True"

# Converting string to boolean
r = "False"
s = bool(r)  # string to boolean (non-empty string is True)
print("Converted string to boolean:", s)  # Output: True (non-empty string is True)

# Converting empty string to boolean
t = ""
u = bool(t)  # empty string to boolean
print("Converted empty string to boolean:", u)  # Output: False (empty string is False)

# Converting list to string
v = [1, 2, 3]
w = str(v)  # list to string
print("Converted list to string:", w)  # Output: "[1, 2, 3]"

# Converting string to list
x = "1,2,3"
y = x.split(",")  # string to list
print("Converted string to list:", y)  # Output: ['1', '2', '3']

# Converting tuple to string
z = (1, 2, 3)
aa = str(z)  # tuple to string
print("Converted tuple to string:", aa)  # Output: "(1, 2, 3)"

# Converting string to tuple
bb = "1,2,3"
cc = tuple(bb.split(","))  # string to tuple
print("Converted string to tuple:", cc)  # Output: ('1', '2', '3')

# Converting dictionary to string
dd = {"a": 1, "b": 2}
ee = str(dd)  # dictionary to string
print("Converted dictionary to string:", ee)  # Output: "{'a': 1, 'b': 2}"

# Converting string to dictionary
import ast
ff = "{'a': 1, 'b': 2}"
gg = ast.literal_eval(ff)  # string to dictionary
print("Converted string to dictionary:", gg)  # Output: {'a': 1, 'b': 2}

# Converting set to string
hh = {1, 2, 3}
ii = str(hh)  # set to string
print("Converted set to string:", ii)  # Output: "{1, 2, 3}"

# Converting string to set
jj = "1,2,3"
kk = set(jj.split(","))  # string to set
print("Converted string to set:", kk)  # Output: {'1', '2', '3'}

# Converting boolean to list
ll = True
mm = [ll]  # boolean to list
print("Converted boolean to list:", mm)  # Output: [True]

# Converting list to boolean
nn = [1, 2, 3]
oo = bool(nn)  # list to boolean (non-empty list is True)
print("Converted list to boolean:", oo)  # Output: True (non-empty list is True)

# Converting empty list to boolean
pp = []
qq = bool(pp)  # empty list to boolean
print("Converted empty list to boolean:", qq)  # Output: False (empty list is False)

# Converting boolean to tuple
rr = False
ss = (rr,)  # boolean to tuple
print("Converted boolean to tuple:", ss)  # Output: (False,)

# Converting tuple to boolean
tt = (1, 2, 3)
uu = bool(tt)  # tuple to boolean (non-empty tuple is True)
print("Converted tuple to boolean:", uu)  # Output: True (non-empty tuple is True)

# Converting empty tuple to boolean
vv = ()
ww = bool(vv)  # empty tuple to boolean
print("Converted empty tuple to boolean:", ww)  # Output: False (empty tuple is False)

# Converting boolean to dictionary
xx = True
yy = {"value": xx}  # boolean to dictionary
print("Converted boolean to dictionary:", yy)  # Output: {'value': True}

# Converting dictionary to boolean
zz = {"a": 1, "b": 2}
aa = bool(zz)  # dictionary to boolean (non-empty dictionary is True)
print("Converted dictionary to boolean:", aa)  # Output: True (non-empty dictionary is True)

# Converting empty dictionary to boolean
bb = {}
cc = bool(bb)  # empty dictionary to boolean
print("Converted empty dictionary to boolean:", cc)  # Output: False (empty dictionary is False)

# Converting boolean to set
dd = False
ee = {dd}  # boolean to set
print("Converted boolean to set:", ee)  # Output: {False}

# Converting set to boolean
ff = {1, 2, 3}
gg = bool(ff)  # set to boolean (non-empty set is True)
print("Converted set to boolean:", gg)  # Output: True (non-empty set is True)

# Converting empty set to boolean
hh = set()
ii = bool(hh)  # empty set to boolean
print("Converted empty set to boolean:", ii)  # Output: False (empty set is False)
