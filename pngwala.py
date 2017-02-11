from PIL import Image
f = open('abc.txt', 'r')
print("reading lines.........")
ls = f.readline()
print("reading lines complete")
ls=ls.replace('[(','').replace(')]','').split("), (")
last= []
for i in ls:
    a=[]
    for j in i.split(", "):
        a.append(int(j))
    last.append(tuple(a))
im = Image.new("RGB", (10000, 500))
im.putdata(last)
im.save("def.png")
print("Image file created")
