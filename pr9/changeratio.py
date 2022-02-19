from PIL import Image as IG
import os
import re

liste =  os.listdir(r'./conv/')
print(f'enter width and height: ')
x = int(input())
for line in liste:
    if re.search(".*.png", line) or re.search(".*.jpg", line)  : 
        img = IG.open(f"./conv/{line}")
        print(img)
        heigh = img.size[1]
        widt = img.size[0]
        print(f'{line}: height: {heigh} width: {widt}')
        ny = int(x*(heigh/widt))
        img = (img.resize((x , ny), IG.ANTIALIAS))
        #name = re.search(,line)
        img.save(f"./after/{x}-{line}")