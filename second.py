def string(str1, str2):
   middleIndex=int(len(str1)/2)
   global middleThree
   middleThree=str1[:middleIndex:]+str2+str1[middleIndex:]
string("Ault","Kelly")
print(middleThree)
