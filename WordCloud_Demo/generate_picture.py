# -- 载入歌词 --
import load_file

content = load_file.load_lyrics('./Lyrics')
print('\n显示部分歌词...\n')
print(content[:100])
print()

# -- 提取关键词 --
import jieba.analyse

# 提取 keyword_num 个关键词以及比重
keyword_num = 800
find_words = jieba.analyse.textrank(content, topK=keyword_num, withWeight=True)
# 生成关键词、比重dict
keyword = dict()
for i in find_words:
    keyword[i[0]] = i[1]
print("'关键词': 比重")
print(keyword)

# -- 生成云图 --
from PIL import Image, ImageSequence
import numpy
import matplotlib.pyplot as pylt
from wordcloud import WordCloud, ImageColorGenerator

# 初始化图片
image = Image.open('./Picture/google.png')
graph = numpy.array(image)

# 生成云图
print('\n云图生成ing...')
# WordCloud 默认不支持中文,需要加载中文字库
words_cloud = WordCloud(font_path='./Fonts/simhei.ttf',background_color='white', max_words=keyword_num, mask=graph)
words_cloud.generate_from_frequencies(keyword)
image_color = ImageColorGenerator(graph)

# 显示图片
pylt.imshow(words_cloud)
pylt.imshow(words_cloud.recolor(color_func=image_color))
pylt.axis("off")  # 关闭图像坐标系
pylt.show()