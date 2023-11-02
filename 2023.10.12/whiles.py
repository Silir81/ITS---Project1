import time

# Python program to illustrate
# while loop
count = 0
while count < 3:
    count = count + 1
    print("Hello world")
    time.sleep(2)  # delay
# # ----------------------------------------------
# An empty loop
# Iterating over a String
some_string = "short while"
i = 0

while i < len(some_string):
    print('Character at position {}: {}'.format(i, some_string[i]))
    i += 1
    pass  # null statement

print('Value of i :', i)