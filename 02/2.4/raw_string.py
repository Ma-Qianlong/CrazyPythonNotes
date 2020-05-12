# 原始字符串

# 原始字符串以r开头
s1 = r'G:\publish\codes\01\003'
print(s1)

# 原始字符串中包含的引号同样需要转义
s2 = r'"Let\'s go", said Charlie'
print(s2)

# 原始字符串中的反斜杠会对引号转义，因此其结尾不能是反斜杠
# 可用 长字符串 来替代， 或件反斜杠单独写，如下
s3 = r'Good Morning' '\\'
print(s3)