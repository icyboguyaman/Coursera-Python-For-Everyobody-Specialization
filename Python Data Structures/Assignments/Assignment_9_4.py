name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
x = 0
counts = dict()
for line in handle :
    if line.find ('From ') : continue
    x = x + 1
    line = line.split()
    mails = line[1]
    counts[mails] = counts.get(mails, 0) + 1
    print("mails", mails)
mostmails = None
prolificomitter = None
for sender,amount in counts.items():
    if mostmails is None or amount > mostmails:
        print("sender, amount", sender, amount)
        mostmails = amount
        prolificomitter = sender
print(prolificomitter, mostmails)
