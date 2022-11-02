# given data
sample = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandallt heKingsmenCouldntputHumptyDumptyinhisplaceagain."
a = 22
b = 27
c = 98
d = 103

# my code
result = ""
for i in range(a, b+1):
    result += sample[i]
result += " "
for i in range(c, d+1):
    result += sample[i]

print(result)
