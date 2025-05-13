import random as r

names = ['Alex', 'Batman', 'George', 'Dave', 'Matthew']
scores = {i: r.randint(0, 100) for i in names}
passed_scores = {i: scores[i] for i in scores if scores[i] >= 40}
print(passed_scores)

sentence = 'Hewwo world, I am Patrick'
word_len = {i: len(i) for i in sentence.split()}
print(word_len)

degrees_c = {'mon': 4, 'tue': 15, 'wed': 24}
degrees_f = {day: degrees_c[day]*1.8 + 32 for day in degrees_c}
print(degrees_f)