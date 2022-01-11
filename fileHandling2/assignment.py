f = open('message.txt', 'r')
#print(len(f.readlines()))
data  = f.readlines()
wc = 0
for x in data:
    words = x.split()
    wc = wc + len(words)

print(wc)
print(len(data))
# display lines, words, chars
# lc= wc = cc = 0
# for line in f:
#     lc = lc +1
#     cc = cc + len(line)
#     temp = line.split()
#     print(temp)
#     wc = wc + len(temp)
#
# print(lc)
# print(cc)
# print(wc)