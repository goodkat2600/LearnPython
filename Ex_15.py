from sys import argv

script = argv

print "Type the filename you want to open:"
file_name = raw_input()

txt = open(file_name)

print txt.read()
txt.close()
