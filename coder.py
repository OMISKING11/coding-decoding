a = "00001"
b = "00010"
c = "00011"
d = "00100"
e = "00101"
f = "00110"
g = "00111"
h = "01000"
i = "01001"
j = "01010"
k = "01011"
l = "01100"
m = "01101"
n = "01110"
o = "01111"
p = "10000"
q = "10001"
r = "10010"
s = "10011"
t = "10100"
u = "10101"
v = "10110"
w = "10111"
x = "11000"
y = "11001"
z = "11010"
space = "00000"

s = str(input("Enter the sentence to be converted to a code: "))
s = s.lower()
s = s.replace(" ", space)
s = s.replace("a", a)
s = s.replace("b", b)
s = s.replace("c", c)
s = s.replace("d", d)
s = s.replace("e", e)
s = s.replace("f", f)
s = s.replace("g", g)
s = s.replace("h", h)
s = s.replace("i", i)
s = s.replace("j", j)
s = s.replace("k", k)
s = s.replace("l", l)
s = s.replace("m", m)
s = s.replace("n", n)
s = s.replace("o", o)
s = s.replace("p", p)
s = s.replace("q", q)
s = s.replace("r", r)
s = s.replace("s", s)
s = s.replace("t", t)
s = s.replace("u", u)
s = s.replace("v", v)
s = s.replace("w", w)
s = s.replace("x", x)
s = s.replace("y", y)
s = s.replace("z", z)
print(s)