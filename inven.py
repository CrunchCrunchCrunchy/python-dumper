def ati(item2add,inv):
    for k in item2add:
        if k not in inv:
            inv.setdefault(k,1)
        else:
            inv[k]+=1
def disinv(inv):
    tot=int(0)
    for k,v in inv.items():
        print(k,v)
    for k,v in inv.items():
        tot+=int(v)
    print(str(tot)+' '+'items total')
            
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
ati(dragonLoot,inv)
disinv(inv)

