import re


word = re.compile(r'(\w*herit\w*)', re.IGNORECASE)

text=''
file = open('origin.txt')
for line in file:
    new_file=open('result.txt','w')
    line_number=0
    line_number+=1
    if word.search(line):
        new_file.write(str(line_number)+"\t"+word.search(line).group(0)+"\n")
new_file.close()





