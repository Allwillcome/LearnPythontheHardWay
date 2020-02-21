#-*- coding: UTF-8 -*-  
my_name = 'Zed A.Shaw'
my_age = 35 # not a line
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name # %s 是字符串
print "He's %d inches tall." % my_height #%d 是单个单词
print "He's %d pounds heavay." % my_height
print "Actually that's not too heavy."
print "He's got %s  eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
print "输出中文尝试"
print u"字符串前加U尝试"


# this line is tricky, try to get it exactly right
print "If I add %d,%d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight) # 字符串可以执行运算运算
