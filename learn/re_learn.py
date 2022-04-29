import re


# . 表示要匹配除了换行符之外的任何单个字符。
# * 表示匹配前面的子表达式任意次，包括0次。
# + 表示匹配前面的子表达式一次或多次，不包括0次。(进行限制)
# ? 表示匹配前面的子表达式0次或1次。
# {} 前面的字符匹串指定的次数. a{3,4},匹配a至少三次, 至多四次 

# source = '<html><head><title>Title</title>'
# want to find ['<html>', '<head>', '<title>', '</title>']
# 很容易想到使用正则表达式 <.*>
#  the result is ['<html><head><title>Title</title>']
# 解决这个问题，就需要使用非贪婪模式，
# 也就是在星号后面加上 ? ，变成这样 <.*?>

# \ 在正则表达式中有多种用途。例如表示字符本身

# 反斜杠后面接一些字符，表示匹配 某种类型 的一个字符。
# \d 匹配0-9之间任意一个数字字符，等价于表达式 [0-9]
# \D 匹配任意一个不是0-9之间的数字字符，等价于表达式 [^0-9]
# \s 匹配任意一个空白字符，包括 空格、tab、换行符等，等价于表达式 [\t\n\r\f\v]
# \S 匹配任意一个非空白字符，等价于表达式 [^ \t\n\r\f\v]
# \w 匹配任意一个文字字符，包括大小写字母、数字、下划线，等价于表达式 [a-zA-Z0-9_]
# 缺省情况也包括 Unicode文字字符，如果指定 ASCII 码标记，则只包括ASCII字母
# \W 匹配任意一个非文字字符，等价于表达式 [^a-zA-Z0-9_]

# [] 表示要匹配 指定的几个字符之一. 
# [abc] 可以匹配 a, b, 或者 c 里面的任意一个字符。等价于 [a-c] 
# 方括号中使用 ^ ， 表示 非方括号里面的字符集合
# [akm.] 匹配 a k m . 里面任意一个字符

# | 表示匹配其中之一

# ^ 表示以什么为开头。
# 注意，compile 的第二个参数 re.M ，指明了使用多行模式
# $ 以什么为结尾

# () 组选择符 
# 可以使用(?P<分组名>表达式)

# 方法
# 1 a.split(str) 使用正则表达式进行切分
# 2 a.sub(rep, str, count = n)   在str中将满足正则条件的字符修改为rep ,最多n次该参数默认为0，即所有的匹配都会替换：



content = '''苹果是绿色的
橙子是橙色的
香蕉是黄色的
乌鸦是黑色的'''

import re
p = re.compile(r'.色')
print(p.findall(content))

print(type(p.findall(content)))
#list

for one in  p.findall(content):
    print(one)

source = '<html><head><title>Title</title>'

import re
p = re.compile(r'<.*>')

print(p.findall(source))


content = '''001-苹果价格-60
002-橙子价格-70
003-香蕉价格-80'''

import re
p = re.compile(r'\d+$', re.MULTILINE)
for one in  p.findall(content):
    print(one)


#分组
content = '''苹果，苹果是绿色的
橙子，橙子是橙色的
香蕉，香蕉是黄色的'''

p = re.compile(r'^(.*)，', re.MULTILINE)

print("测试-分组")
for one in  p.findall(content):
    print(one)



content = '''
<div class="el">
        <p class="t1">           
            <span>
                <a>Python开发工程师</a>
            </span>
        </p>
        <span class="t2">南京</span>
        <span class="t3">1.5-2万/月</span>
</div>
<div class="el">
        <p class="t1">
            <span>
                <a>java开发工程师</a>
            </span>
		</p>
        <span class="t2">苏州</span>
        <span class="t3">1.5-2/月</span>
</div>
'''

import re
p = re.compile(r'class=\"t1\">.*?<a>(.*?)</a>', re.DOTALL)
for one in  p.findall(content):
    print(one)





names = '关羽; 张飞, 赵云,   马超, 黄忠  李逵'

namelist = re.split(r'[;,\s]\s*', names)
print(namelist)