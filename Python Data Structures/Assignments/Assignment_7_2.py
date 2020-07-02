fname = input("Enter file name: ")
fh = open(fname)
n = 0 # for amount of lines
n1 = 0 #for summ
xDSPAM = 0
nfloat = float(n)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    n = n + 1
    xDSPAM = line[line.find('0') : ]
    xDSPAMfl = float(xDSPAM)
    n1 = n1 + xDSPAMfl
median = n1 / n
print("Average spam confidence:", median)