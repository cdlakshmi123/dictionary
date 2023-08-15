# dic={"ball":"red",  "bat":4, "wickets":8, "ball":"green", "bat":3}
# temp = []
# res = dict()
# for key, val in dic.items():
#     if val not in temp:
#       temp.append(val)
#       res[key] = val
# print(res)
dict=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
# temp=[]
# res=dict()
# for key, val in dict.items():
#     if val not in temp:
#         temp.append(val)
#         res[key]=val
# print(res)
sum=0
for i in dict.values():
    for items in i:
        sum+=1
print(sum)

