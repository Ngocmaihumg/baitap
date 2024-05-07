
list_goc = [10,9,8,7,6,1,2,3,4,5]
list_moi = list(filter(lambda a: (a%2 == 0), list_goc))

print (list_moi)

#mảng mới
mang_moi = []
def mangsochan(a):
    for i in a:
        if(i%2==0):
            mang_moi.append(i)
list=[10,9,8,7,6,1,2,3,4,5]
mangsochan(list)
print(mang_moi)