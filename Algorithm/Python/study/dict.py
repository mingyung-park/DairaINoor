dic_3 = {'name': 'mingyung', 'age':4000, 'pet':{'type':'beta','name':'pearl','age':2}}
print(dic_3)

keys=['name','age','pet']
values = ['mingyung',4000,{'type':'beta','name':'pearl','age':2}]
dic_4 = dict.fromkeys(keys,0)
print(dic_4)