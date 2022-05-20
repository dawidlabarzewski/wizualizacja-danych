import numpy as np

# a = np.array([20, 30, 40, 50])
# b = np.array(4)


# c = a + b
# print(c)

# d = np.sqrt(20)
# print(d)

# e = d + c
# print(e)


# a = np.arange(12).reshape((3, 4))
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.sum(axis=1))
# print(a.cumsum(axis=1))


# a = np.arange(3)
# b = np.arange(3)
# print(np.dot(a, b))
# print(a.dot(b))

# c = np.arange(3)
# d = np.array([[0], [1], [2]])
# print(c.dot(d))

# e = np.array([
#     [2, 5, 1],
#     [3, 4, 5]
# ])
# f = np.array([
#     [3, 4],
#     [1, 6],
#     [3, 3]
# ])
# print(e.dot(f))


# a = np.arange(6).reshape((3, 2))
# print(a.flat)

# for b in a:
#     for c in b:
#         print(c)
# for d in a.flat:
#     print(d)


a = np.arange(12).reshape((3, 4))
print(a)
b = a.reshape((4, 3))
print(b)
c = b.ravel()
print(c)
d = b.T
print(d)