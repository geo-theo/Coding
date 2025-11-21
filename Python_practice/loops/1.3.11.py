# What are m and n after the following code is executed?

n = 123456789
m = 0
while n != 0:
    m = (10 * m) + (n % 10)
    n //= 10

print("Answer M: " + str(m))
print("Answer N: " + str(n))



