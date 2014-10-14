
import re
string = '''this is test line.
this is the second line.
today is sunday.'''

match = re.search('(?m)^today',string)

if match:
    print('所使用的正则表达式是：',match.re)
    print('所输入的字符串是：',match.string)
    print('匹配的结果是：',match.group(0))
    print(match.span())
else:
    print('return the none value')

