from operator import add, mul
o1 = add(4, mul(9, mul(add(4, mul(4, 6)), add(3, 5))))
print (o1)

shakes = open('shakespeare.txt')
text = shakes.read().split()
print (len(text))
print (text[:25])

print (text.count("you"))

# 集合（set）是一个无序的不重复元素序列。
words = set(text)

# 直接使用max返回一个字符串里按字母表排序的最长子字符串，从第一个开始一次比较。
# max中声明key=len可以返回长度最长的字符串
print (len(words), max(words), max(words, key=len))


print ("draw"[::-1])
print ({w for w in words if w == w[::-1] and len(w)>4})
print ({w for w in words if w[::-1] in words and len(w)==4})