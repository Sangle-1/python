#!/root/nsd1905/bin/python3
#对比文件不同
a1=input('请输入要对比的第一个文件路径:')
a2=input('请输入要对比的第二个文件路径:')
with open(a1) as f1:
    aset = set(f1)
with open(a2) as f2:
    bset = set(f2)
with open('/tmp/result.txt', 'w') as f3:
     f3.writelines(bset - aset)
print('文件较比后的差异文件放在路径/tmp/result.txt中')
