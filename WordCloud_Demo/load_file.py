import os

# 读取目录下的歌词文件并合成一个字符串返回
def load_lyrics(path):

    content = ''  # 初始化

    for f in os.listdir(path):
        # 得到完整路径
        full_path = os.path.join(path, f)
        # 判断是否是文件
        if os.path.isfile(full_path):
            print('loading {}'.format(full_path))
            # 将歌词读入字符串
            with open(full_path, 'r') as lyrics:
                content += lyrics.read()
                content += '\n'
    print('loading completely')

    # 返回全部歌词
    return content
