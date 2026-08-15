# write a python program to check whether the given list is palindrome or not
list=[1,2,3,2,1]
copy_list=list.copy()
copy_list.reverse()
if copy_list==list:
    print("palindrome")
else:
    print("not palindrome")    