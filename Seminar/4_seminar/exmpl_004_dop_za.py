# Сколько раз встречается цифра в списке, например 5
# sp = [55.1245, 44 ,"5ррууу55",   [95.45,0.5] , {53:  125} ]
# ответ -11

sp = [55.1245, 44 ,"5ррууу55",   [95.45,0.5] , {53:  125} ]
n=str(input ("Сколько раз сдвинуть? "))

stroku=""
for k in sp:
  stroku=stroku+str(k)

count=0
for i in range(len(stroku)):
  if(stroku[i])==n:
    count+=1
    
print (count)