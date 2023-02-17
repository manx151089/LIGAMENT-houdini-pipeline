node = hou.pwd()
geo = node.geometry()
menu = []
prim = geo.iterPrims()[0]
cc = prim.clipCatalog()

for each in cc:
    menu.append(each.name())
    menu.append(each.name())
    
return menu