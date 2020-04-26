list_mRa=[3,5,8,2]
list_aRm=[2,7,4,3,0]
list_mRa+list_aRm
print(list_mRa)
print(list_mRa+list_aRm)
list_mRa.extend(list_aRm)
print(list_mRa)


def maktab(arg):
    list_1.pop()
    list_2.append(3)


list_1=[8,12,10,9]
list_2=list_1
list_1.pop(1)
list_3=list_1
maktab(list_2)
sum_list=sum(list_3)
print(sum_list)


brain=" Know yourself! Understand yourself! Correct yourself! "
brain=brain.strip()
change=brain.split("yourself!")
print(len(change))