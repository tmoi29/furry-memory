f = open("howToSki.txt", "r")
txt = f.read()
f.close()

words = txt.lower().split()
for i in range(len(words)):
    words[i] = words[i].strip('";./()-_?,').lower()

print words

def freq_word(s):
    l = [1 for x in words if x == s.lower()]
    if len(l) == 0:
        return 0
    return len(l)

print freq_word("the")

def freq_phrase(l):
    l2 = [1 for x in words if x.lower() in l]
    return reduce((lambda a, b: a + b), l2)

print freq_phrase(["the","ski"])

def most_freq():
    s = set(words)
    print s
    l = [freq_word(x) for x in words]
    i = l.index(max(l))
    return s[i]

print most_freq()