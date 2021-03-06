from django.shortcuts import render,redirect
import jieba.posseg  # 需要另外加载一个词性标注模块

def fenci(request):
    string = '爱因斯坦其实大家买中国深圳手机就是看个心情！天河区孔子没必要比来比去的红十字会七月十五日。'
    dd = main(string)
    content = {'data': dd}
    return render(request, 'booktest/result.html', content)

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def fenci2(request):
    txt = request.POST['txt']
    dd = main(txt)
    content = {'data': dd}
    return render(request, 'booktest/result.html', content)

def index(request):
    return render(request,'booktest/index.html')


import jieba

import jieba.posseg  # 需要另外加载一个词性标注模块


# 分词并标注词性


def cut_sentence(sentence):
    """
    分句
    :param sentence:
    :return:
    """

    delimiters = frozenset(u'。！？')
    buf = []
    listt = []
    for ch in sentence:
        buf.append(ch)
        if delimiters.__contains__(ch):
            listt.append(''.join(buf))
            buf = []
    return listt


import codecs


def load_stopwords(path=u'C:/Users/linhongcun/PycharmProjects/txt/static/data/stop_word.txt'):
    """
    加载停用词
    :param path:
    :return:
    """
    #    with open(path) as f:
    #        stopwords = filter(lambda x: x, map(lambda x: x.strip().decode('utf-8'), f.readlines()))
    stopwords = [line.strip() for line in codecs.open(path, 'r', encoding='utf8').readlines()]
    stopwords.extend([' ', '\t', '\n'])
    return frozenset(stopwords)


def cut_words(sentence):
    """
    分词
    :param sentence:
    :return:
    """
    stopwords = load_stopwords()
    seg = jieba.posseg.cut(sentence)
    result = []
    for item in seg:
        if not stopwords.__contains__(item.word):
            result.append([item.word, item.flag])
    return result


def main(text):
    tem = cut_sentence(text)
    result = []
    for i in range(len(tem)):
        result.append(cut_words(tem[i]))
    return result