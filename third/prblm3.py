# given data
str = "GATGGAACTTGACTACGTAAATT"
# my code
result = ""
for letter in str:
    if letter == 'T':
        result += 'U'
    else:
        result += letter

print(result)
