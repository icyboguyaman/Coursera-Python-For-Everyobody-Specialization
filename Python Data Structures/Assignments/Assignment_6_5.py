text = "X-DSPAM-Confidence:    0.8475";
digit0 = text.find('0')
digit5 = text.find('5')
number = text[digit0 : digit5+1]
numberfloat = float(number)
print(numberfloat)
