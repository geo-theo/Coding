# What is the value of j after each of the following code fragments is executed?

j = 0
for i in range(0, 10):
   j += i
print("Answer A: " + str(j))

j = 1
for i in range(0, 10):
   j += j
print("Answer B: " + str(j))

for j in range(0, 10):
    j += j
print("Answer C: " + str(j))

