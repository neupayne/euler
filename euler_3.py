print 'Welcome to the Pig Latin Translator!'

raw_input ("Enter a word:")
original = raw_input()

if len(original) > 0 and original.isalpha() :
    print original
else :
    print "empty"

