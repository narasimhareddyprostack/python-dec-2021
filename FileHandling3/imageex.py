#wap to create new image based on existig image.
#image is part binary file.

f2 = open('just.jpeg', 'rb')
bytes=f2.read()

f1 = open('newlogo.png', 'wb')
f1.write(bytes)


