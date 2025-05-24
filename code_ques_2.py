plyrs= int(input()) #1-8

l= max(14,plyrs*4)
ar_ct= max(1,plyrs//2)
usd_rms= 1+2+(ar_ct*4)
cor_ct= l-usd_rms

dngn= []
dngn.append("SHRINE")

for i in range(cor_ct//2):
    dngn.append("CORRIDOR")

for i in range(ar_ct):
    dngn.append("CROSSROADS")
    dngn.append("SHRINE")
    dngn.append("ARENA")
    dngn.append("TREASURE")

for i in range(cor_ct- cor_ct//2):
    dngn.append("CORRIDOR")

dngn.append("BOSS")
dngn.append("TREASURE")

for rm in dngn:
    print(rm)