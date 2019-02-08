# reverse string
word = "hello world"

new = ""
for letter in word:
    new = letter + new
print(new)
# dlrow olleh

# or using extended slices
print(word[::-1])
# dlrow olleh