dic={}
print(dic)
print(type(dic))
dic['name']='mano'
print(dic)
dic.update({'degree':'b.bom','d_o_b':12_2_2003,'native':'tenkasi',43:'id'})
print(dic)
dic['name']='mariappan'
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
print('name:',dic['name'])
print('i am from:',dic.get('native'))
print(len(dic))
dic.pop('degree')
print(dic)
del dic[43]             
print(dic)
