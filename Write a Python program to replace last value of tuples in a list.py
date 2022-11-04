l = [(10, 20, 40),(40, 50, 60),(70, 80, 90)]
print(l)
print(list(t[:-1] + (200,) for t in l))
