import re
data_dir="/content/data"
file=open(data_dir+"/conll-2012/v3/scripts/skeleton2conll.py","r")
text=file.read()
text=re.sub("except InvalidSexprException, e","except InvalidSexprException as e",text)
text=re.sub("print\n","print()\n",text)

def addbracket(matched):
    return "print("+matched.group("source")+")\n"
 
text=re.sub('print (?P<source>.*)\n', addbracket, text)
print(text)
file.close()
file=open(data_dir+"/conll-2012/v3/scripts/skeleton2conll.py","w")
file.write(text)
file.close()
