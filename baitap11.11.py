b=()
for x in range(10):
    a=input('Nhập phần tứ thứ '+str(x+1)+':')
    b+=(a,)
print('Tuple:',b)
i=int(input('Nhập số từ 0 đến 9:'))
j=int(input('Nhập số từ -1 đến -9:'))
s_find=input('Nhập chuỗi cần tim:')
print('Tuple[%i]='%(i),b[i])
print('Tuple[%i]='%(j),b[j])
print(s_find,'xuất hiện trong tuple %i lần'%(b.count(s_find)))







