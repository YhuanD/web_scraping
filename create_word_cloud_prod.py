# -*-coding:utf-8-*-
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
	reload(sys)
	sys.setdefaultencoding(defaultencoding)
from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba

jieba.load_userdict("new_words_add.txt")

def trans_CN(text):
	word_list = jieba.cut(text)
	result = " ".join(word_list)
	return result

with open("jobs_titles_prod.txt") as fp:
	text = fp.read()
	text = text.replace(u"腾讯",u"")
	text = text.replace(u"深圳",u"")
	text = text.replace(u"及",u"")
	text = text.replace(u" ",u"")
	text = text.replace(u"工程师",u"")
	text = trans_CN(text)
	print(text)
	wordcloud = WordCloud(font_path="simfang.ttf").generate(text)
	image_produce = wordcloud.to_image()
	image_produce.show()


