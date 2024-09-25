str = "Tanmoy Santra"
print("The string = ",str)
#lower
print("Lower = ",str.lower())
#upper
print("Upper = ",str.upper())
#strip
str1 = (" One day ")
print("Strip = ",str1.strip())
#rstrip
str1 = "Tanmoy yyyyy"
print("Rstrip = ",str1.rstrip("y"))
#replace
print("Replace = ",str.replace("an","@"))
#spilt
print("Spilt = ",str.split())
#capitalize
str1 = "mango ice cream"
print("Capitalize = ",str1.capitalize())
#center
print(str.center(60))
#count
print("Count = ",str.count("a"))
#endswith
print("Endswith \"tra\" = ",str.endswith("tra"));
print("Endswith \"oy\" = ",str.endswith("oy"));
#find
print("find = ",str.find("a"))
print("find = ",str.find("u"))
#index
print("Index = ",str.find("n"))
#inalnum
str1 = "ABCefg019"
print("Alphanumeric = ",str1.isalnum())
str2 = "ABCefg019%$"
print("Alphanumeric = ",str2.isalnum())
#isalpha
str1 = "ABCefh"
print("Alphanumeric = ",str1.isalpha())
str2 = "ABCefg019"
print("Alphanumeric = ",str2.isalpha())
#islower
str1 = "abchtanm"
print("Islower = ",str1.islower())
str2 = "ANgdh"
print("Islower = ",str2.islower())
#isupper
str1 = "ABCDTANMO"
print("Isupper = ",str1.isupper())
str2 = "ANjkdoe"
print("Isupper = ",str2.isupper())
#isprintable
str1 = "ABCDTANMO09!^"
print("Isprintable = ",str1.isprintable())
str2 = "ANjkdoe\n"
print("Isprintable = ",str2.isprintable())