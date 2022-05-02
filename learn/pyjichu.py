###string

#1. 其值不可变

#赋值新字符串

print("1")
name = 'name1'
age = 18
s1 = 'my name is {} age is {}'.format(name, age)

s2 = f'my name is {name},age is {age}'

s3 = "my name is %s my age is %s" %(name, age)
print(s1,s2,s3)

#分隔字符串为列表
l1 = s1.split()

#按照某个字符分隔   str.split(ch, n)
l1 = s1.split('e',1);

#计算字符出现次数
a = s1.count('e');

#替换字符
s4 = s1.replace('e', 'Ee', 2)

print(s4)


#list
l1 = ['1', '2', '3'];

#末尾添加元素
l1.append("4")
#末尾删除元素
l1.pop()
#删除指定元素
l1.pop(0);

#列表可以进行相加 “+” 和相乘 “*” 运算，
# “+” 相当于拼接列表，“*” 相当于重复列表。

#列表推导式的一般语法结构：
# new_list = [x for x in iterable]
#其中的 iterable 表示可迭代的对象，包括字符串（str）、列表（list），
# 元组（tuple）、字典（dict）、集合（set），以及生成器（generator）等。

#列表推导式中还可以引入 if 条件语句，如下
if_list = [x**2 for x in range(10) if x%2==0]
print(if_list)