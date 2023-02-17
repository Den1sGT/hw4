import turtle as t

t.speed(15)
t.color('red')
t.bgcolor('white')
b = 200

while b > 0:
    t.left(b)
    t.forward(b * 3)
    b = b - 1
t.done()