#!/usr/bin/env python
from PIL import Image, ImageFont, ImageDraw

A4_h = 3508
A4_b = 2480

Letter_h = 816
Letter_b = 1056

#costum size in mm:
h = 161
b = 229

#converting to px [(mm × 96) ÷ 25.4 = px]

h = round((h * 96) / 25.4)
b = round((b * 96) / 25.4)

list_name = []
fil = open("adress.txt", encoding='utf-8')
list_mock = fil.readlines()
fil.close()

for name in list_mock:
    list_name.append(name.strip("\n"))


def draw_row(row, font, pos_x, pos_y, draw, fontsize, buff):
    fontt = ImageFont.truetype(font, fontsize)
    
    left, top, right, bottom = fontt.getbbox(row)
    width = right - left
    if width + buff < pos_x:
        draw.text((pos_x, pos_y), row, font=fontt, fill="black")
        pos_y += fontsize 
        return pos_y
           
        
    else:
        pos_y = draw_row(row, font, pos_x, pos_y, draw, fontsize-2, buff)
        return pos_y
        
        
    

def make_nametag(list_of_names, paper_w, paper_h, num_w, num_h, font, fontsize, pagenum, buff):
    # Background
    img = Image.new("RGB", (paper_w, paper_h), "white")
    draw = ImageDraw.Draw(img)
    pos_x = (paper_w/2)
    pos_y = (paper_h/2) + (buff*2)
    
    for row in list_of_names:
        #cap = row.split(" ")
        #row = ""
        #for n in cap:
        #    row = row + n.capitalize() + " "
            
        pos_y =  draw_row(row, font, pos_x, pos_y, draw, fontsize, buff)

    
    img = img.save("Brev{}.jpg".format(pagenum))

def main(list_of_names, paper_w, paper_h, num_w, num_h, font, fontsize, buff):
    fil_num = 1
    fil_st = num_h*num_w

    while len(list_of_names) > fil_st:
        make_nametag(list_of_names[:fil_st], paper_w, paper_h, num_w, num_h, font, fontsize, fil_num, buff)
        fil_num += 1
        list_of_names = list_of_names[fil_st:]
    make_nametag(list_of_names, paper_w, paper_h, num_w, num_h, font, fontsize, fil_num, buff)


main(list_name, A4_h, A4_b, 1, 4, "fonts/Myfont-Regular.ttf",200, 200)



