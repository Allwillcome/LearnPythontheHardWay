# coding=utf-8 
import random
from urllib import urlopen
import sys
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
        "class ### (###):":
        "Make a class named ### that is-a ###.",
        "class ###(object):\n\tdef __init__(self,***)": "class ### has-a __init__that takes self and *** parameters.",
        "class ###(object):\n\tdef ***(self,@@@)": "class ### has-a function named *** that takes self and @@@ parameters.",
        "*** = ###()":"Set *** to an instance of class ###.",
        "***.***(@@@)":"From *** get the *** function, and call it with parameters self, @@@.",
        "From *** get the'***'": "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_First = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_First = True
    
# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())
    
    
def convert(snippet, phrase):
    class_name = [w.capitalize() for w in
                random.sample(WORDS, snippet.count("***"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
    
    for i in range(0, snippet.count("@@@")):
        paran_count = random.randint(1,3)
        param_name.append(','.join(random.sample(WORDS, param_count)))
        
    for sentence in snippet, phrase:
        result = sentence[:]
        
        # fake class names
        for word in class_name:
         result = result.replace("###",word,1)
         
        # fake other names
        for word in param_names:
            result = result.replace("@@@",word, 1)
            
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@",word,1)
            
        results.append(result)
         
        return results
         
# keep going until they hit CTRL-D
try: 
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question,answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question,answer = answer,question
                
            print question
            
            raw_input(">")
            print "ANSWER: %S\n\n" %answer
except EOFError:
        print "\nBye"
        

            
       
    