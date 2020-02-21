from sys import argv
# import moudle
script, user_name = argv
prompt = '>'
# define prompt
print "Hi %s, I am the %s script." %(user_name, script) #import user_name
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
