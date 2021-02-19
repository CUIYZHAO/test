n=int(input('请输入十进制整数：'))
lst=[]
while n>0:
    lst.insert(0,n%2)
    n=n//2
print(''.join(map(str,lst)))
