name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
x = 0
counts = dict()
for line in handle :
    if line.find ('From ') : continue
    x = x + 1
    line = line.split()
    line = line[5]
    line = line.split(':')
    line = line[0]
    counts[line] =  counts.get(line, 0) + 1#Hystagramm growth by 1 block
print("counts unsorted", counts)# hystagramm result unsorted
counts = sorted(counts.items())
print("counts sorted", counts)# hystagramm result sorted by str
for hours, times in counts:
    print(hours,times)
