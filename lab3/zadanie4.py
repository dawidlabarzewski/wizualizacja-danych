def is_rectangular_triangle(a, b, c):
    a **= 2
    b **= 2
    c **= 2
    return (a + b == c) or (a + c == b) or (b + c == a)

print(is_rectangular_triangle(3,4,5))
print(is_rectangular_triangle(3,4,6))
print(is_rectangular_triangle(6,10,8))