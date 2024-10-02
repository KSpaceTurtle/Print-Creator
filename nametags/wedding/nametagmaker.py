#!/usr/bin/env python
from PIL import Image, ImageFont, ImageDraw


# Bearbetar textfilen till en lista men namn som element.
list_name = []
fil = open("guests.txt", encoding='utf-8')
list_mock = fil.readlines()
fil.close()

for name in list_mock:
    list_name.append(name.strip("\n"))


def make_nametag(list_of_names, paper_w, paper_h, num_w, num_h, font, fontsize, pagenum):
    box_w = paper_w/num_w
    box_h = paper_h/num_h

    cor_x = 0
    cor_y = 0

    font = ImageFont.truetype(font, fontsize)
    # Bakrunden till namnlapparna
    img = Image.new("RGB", (paper_w, paper_h), "white")
    draw = ImageDraw.Draw(img)

    # Skrivan namnen
    for name in list_of_names:
        cap = name.split(" ")
        name = ""
        for n in cap:
            name = name + n.capitalize() + " "
        
        left, top, right, bottom = font.getbbox(name)
        width = right - left
        height = bottom - top
        pos_x = (box_w-width)/2
        pos_y = box_h - (box_h-height)/2
        
        if width > box_w*0.9:
            ful_name = name.split(" ")
            y_fix = -fontsize/2
            
            for parts in ful_name:
                left, top, right, bottom = font.getbbox(parts)
                width = right - left
                height = bottom - top
                pos_x = (box_w-width)/2
                pos_y = box_h - (box_h-height)/2
                draw.text((pos_x + cor_x, pos_y + cor_y - box_h/10 + y_fix), parts, font=font, fill="black")
                y_fix = y_fix + fontsize
                
            cor_x += box_w    
        else:
            draw.text((pos_x + cor_x, pos_y + cor_y - box_h/10), name, font=font, fill="black")
            cor_x += box_w
            
        if pos_x + cor_x > paper_w:
            cor_x = 0
            cor_y += box_h

    img = img.save("wedding_guests_s.{}.jpg".format(pagenum))


def main(list_of_names, paper_w, paper_h, num_w, num_h, font, fontsize):
    fil_num = 1
    fil_st = num_h*num_w

    while len(list_of_names) > fil_st:
        make_nametag(list_of_names[:fil_st], paper_w, paper_h, num_w, num_h, font, fontsize, fil_num)
        fil_num += 1
        list_of_names = list_of_names[fil_st:]
    make_nametag(list_of_names, paper_w, paper_h, num_w, num_h, font, fontsize, fil_num)


#main(list_name, 2480, 3508, 2, 5, "fonts/Demo_ConeriaScript_Slanted.ttf",150)
main(list_name, 2480, 3508, 2, 8, "fonts/Demo_ConeriaScript.ttf",90)
#main(list_name, 2480, 3508, 2, 5, "fonts/Astrid.otf",150)
#main(list_name, 2480, 3508, 2, 5, "fonts/South Rattingson.otf",150)



