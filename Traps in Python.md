## Traps in Python

[TOC]

### try except 输出具体的行号

try except 无法直接定位到具体存在问题的代码位置

```python
try:
    pass
except Exception as e:
    # 输出异常的文件名
    print(e.__traceback__.tb_frame.f_globals['__file__'])
    # 输出异常代码所在的行号
    print(e.__traceback__.tb_lineno)
    print(e)
```

### 读取文件的默认使用 ascii

在 python3 中，默认使用的是 utf 的编码格式，但在有些情况下，会使用 ascii 编码进行文件解析，报出以下异常：

```bash
$ 'ascii' codec can't decode byte 0xe8 in position
```

网上推荐的方法为设置默认的编码格式：

```python
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
```

但是以上代码只适用于 python2，不适用与 python3。

最简单的方法，是在文件读取时，设定好默认的编码格式：

```python
with open("path", "r", encoding = "utf-8") as file:
    pass
```

### 使用 utf-8 读取文件存在解析异常

可以尝试使用 `latin_1` 的编码方式，尝试打开文件

