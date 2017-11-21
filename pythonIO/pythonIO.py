f = open('example.txt')

text = f.read()

f.close()

# Automatically close text file once done
with open('example.txt', 'w') as f:
    f.write("Test words")

with open('example.txt') as f:
    text = f.read()
    print(text)

with open("example.txt", 'a') as f:
    f.write('line 1 \n')
    f.write('line 2 \n')

with open('example.txt') as f:
