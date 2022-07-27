# TODO gensim引入错误需解决
import gensim   #首次需要install
from gensim.models import KeyedVectors, Word2Vec

#分词
import re
import jieba  #首次需要安装
import jieba.analyse

stop_words = []
cut_result = open('data/after_cut.txt', 'w', encoding='UTF-8')

def cut_words(filepath):
    with open(filepath, 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            word_list = []
            #过滤掉所有的标点符号
            punctuation = r"~!@#$%^&*()_+`{}|\[\]\:\";\-\\\='<>?,./，。、《》？；：‘“{【】}|、！@#￥%……&*（）——+=-"
            line = re.sub(r'[{}]+'.format(punctuation), '', line)
            #去掉换行和空格
            # line = line.replace("\n", "").replace("\r", "").strip()
            words = jieba.lcut(line)
            for word in words:
                if (word not in stop_words):
                    word_list.append(word)
            cut_result.write('  '.join(word_list))
            cut_result.flush()

cut_words("data/test_data.txt")


#调用Word2Vec
model = Word2Vec(stop_words, vector_size=20, window=2, min_count=3, epochs=7, negative=10)
print('西棠的词向量：\n', model.wv.get_vector('西棠'))
print('\n和西棠相关性最高的20个词语：')
model.wv.most_similar('西棠',topn=20)