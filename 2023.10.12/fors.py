# # Iterating over a list
# l = ["geeks", "for", "geeks"]
#
# for i in l:
#     print(i)
# ----------------------------------------------
# Iterating over dictionary
# print("Dictionary Iteration")
#
# d = dict()
#
# d['xyz'] = 123
# d['abc'] = 345
# for i in d:
#     print("Dictionary key: {}, dictionary value: {}".format(i, d[i]))

temp = 12
voltage = 12
current = 0.03
print("Ambient temp is: " + str(temp) + " measured voltage: " + str(voltage) + " measured current: " + str(current))
print("Ambient temp is: {} measured voltage: {} measured current: {:d}".format(temp, voltage, int(current)))
#
# temp = 11
# voltage = 13
# current = 0.012
# print("Ambient temp is: " + str(temp) + " measured voltage: " + str(voltage) + " measured current: " + str(current))
# # ----------------------------------------------
# Iterating over a String
# print("String Iteration")
#
# s = "some kind of monster"
# for i in s:
#     print(i)
# # ----------------------------------------------

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
