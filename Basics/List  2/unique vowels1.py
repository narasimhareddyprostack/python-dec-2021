count = []
word = "Helloou"
for char in word:
    if char in ['a','e','i','o','u']:
        if char not in count:
            count.append(char)
	   

print(count)
print("No of unique vowels", len(count))
