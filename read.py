import re

text=''
file = open('origin.txt')
for line in file:
    text = text+line
file.close()

word = re.compile(r'(\w*herit\w*)', re.IGNORECASE)

new_file=open('result.txt','w')
line_number=0
for line in text:
    line_number+=1
    if word.match(line):
        new_file.write(str(line_number)+"\t"+str(match.group(0))+"\n")
new_file.close()





