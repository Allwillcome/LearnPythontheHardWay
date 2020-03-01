#coding=utf-8
import random
from urllib import urlopen
import sys
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
        "class %%%(%%%):": "Make a class named %%% that is-a %%%.",
        "class %%%(object):\n\tdef __init__(self,***)":"class %%% has-a __init__that takes self and *** parameters.",
        "class %%%(object):\n\tdef __init__(self,@@@)":"class %%% has-a function named ***_that takes self and @@@ parameters.",
        "*** = %%%()":"Set *** to an instance of class %%%.",
        "***.***(@@@)":"From *** get the *** function,and call it with parameters self,@@@.",
        "From *** get the '***'":"From *** get the *** attribute and set it to '***'."
        }

# do they want drill phrase first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":                 #sys.argv获取输入的参数值
    PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())     
    #.strip()用于移除字符串首尾字符，默认为空格

print WORDS

def convert(snippet,phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS,snippet.count("%%%"))] #captitalize()将第一个首字母大写，其余全部小写  count()统计snippt中出现字符串%%%的个数
    other_names = random.sample(WORDS,snippet.count("***"))                     #random.sample()可以从指定的序列中，随机的截取指定长度的片断，不作原地修改。
    print "*"*20
    print "class_name are:\n", class_names
    print "other_names are:\n",other_names
    print "*"*20
    results = []
    param_names = []

    for i in range(0,snippet.count("@@@")):
        param_count = random.randint(1,3)                               #random.randint()随机生一个整数int类型，可以指定这个整数的范围，同样有上限和下限值
        param_names.append(','.join(random.sample(WORDS,param_count)))  #.join()将序列中的元素以指定的字符连接生成一个新的字符串。

    for sentence in snippet,phrase:
        result = sentence[:]                                            #python中复制列表的方法

        #fake class names
        for word in class_names:
            result = result.replace("%%%",word,1)                       # replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

        #fake other names
        for word in other_names:
            result = result.replace("***",word,1)

        #fake parameter lists
        for word in param_names:
            result = result.replace("@@@",word,1)

        results.append(result)
    return results

#keep going until they hit CTRL-D
try:
    while True:

        snippets = PHRASES.keys()                                       #Python 字典(Dictionary) keys() 函数以列表返回一个字典所有的键
        print "Keys in PHRASES are:\n %s",snippets

        random.shuffle(snippets)                                       #random.shuffle()如果你想将一个序列中的元素，随机打乱的话可以用这个函数方法。 
        for snippet in snippets:
            phrase = PHRASES[snippet]
            print "phrase: %s  ----> snippet: %s \n"%(phrase,snippet)
            question,answer = convert(snippet,phrase)
            print "*"*20
            print "question:\n",question
            print "answer:\n",answer

            if PHRASE_FIRST:
                question,answer = answer,question
            print "*"*20
            print question

            raw_input(">")
            print "ANSWER:%s\n\n"%answer
except EOFError:
    print "\nBye"