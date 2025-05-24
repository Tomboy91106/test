lst= [5, 3, 2, 8, 4, 5, 2, 1, 9, 5, 3]
lst.sort(reverse=False)

new_lst=[]
rem= []
for n in lst:
    if n not in new_lst:
        new_lst.append(n)
    else:
        rem.append(n)

fin_lst= new_lst + rem
print("Ordered list= ", fin_lst)