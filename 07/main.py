nm = "TanmoySantra"
nm_len = len(nm) #store the length of the string into nm_len variable
print("Length of ",nm," is = ",nm_len)

#slicing
print(nm[0:5]) #index 0 to index 4 (5-1)
print(nm[:4])  #index 0 to index 3 (4-1). blank means 0 index
print(nm[1:4]) #index 1 to index 3 (4-1)
print(nm[:])   #index 0 to length of the string
print(nm[0:-2])  #index 0 to 9 ((length-2)-1)
print(nm[-4:-1]) #index 8 (length-4) to index 10 ((length-1)-1)
print(nm[nm_len-4:nm_len-1]) #same as above

#print string using loop
for ch in nm:
    print(ch, end=" ")