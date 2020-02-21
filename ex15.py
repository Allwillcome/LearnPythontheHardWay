from sys import argv
# import mouldes
script, filename = argv

txt = open(filename)
# define the txt
print "Here's your file %r :" % filename
print txt.read()
# implement reading text content
print "Type the filename again:"
file_again = raw_input(">")

txt_again = open (file_again)

print txt_again.read()
