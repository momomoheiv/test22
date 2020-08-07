
# 文件写入
def write_file(file_path, content):
    """
        方法：写入文件
        参数：
            - file_path:要写入的文件路径
            - content：要写入的内容
    """
    with open(file_path, 'w') as f:
        f.write(content)

# 文件读取
def read_file(file_path):
    """
        方法：读取文件
        参数：
            - file_path:要写入的文件路径
        返回值：返回文件的字符串
    """
    with open(file_path, 'r') as f:
        t = f.readline()

    return t



# write_file('a.txt', "python testing!")
# res = read_file('a.txt')  # res= 文件的内容
# print(res)