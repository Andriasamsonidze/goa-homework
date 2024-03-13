result = int(input("რა ქულა მიიღე ტესტში?:  "))
if result > 90 and result < 100:
    print("თქვენ დაგიფინანსდებათ სწავლა სრულიად")
elif result > 70 and result < 80:
    print("თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით")
elif result > 40 and result < 70:
   print("თქვენ დაგიფინანსდათ სწავლა 500 ლარით")
else:
    print("თქვენ არ დაგიფინანსდათ სწავლა")      