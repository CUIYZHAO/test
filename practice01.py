x=input()
students={}
scores={}
sx=str(x)
s=x.split(',')
while True:
    if sx=='END':
        break
    if len(s)==2:
        #2020205001,Cui
        students[s[0]]=s[1]
    if len(s)==3:
        #2020205001,Math,90
        d=scores.get(s[0],{})
        d[s[1]]=int(s[2])
        scores[s[0]]=d
    print(students)
print(f'{students[0]}\t{scores[student[0]]}')
