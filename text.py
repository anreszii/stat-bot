
def sizer(size,im):
    print(size)
    if size == [1341, 1920]:
        sc1 = calc("s",840,170,100,70,0,0)
        sc2 = calc("s",980,170,100,70,0,0)
        p1 = calc("p",190,280,430,68,0,68)
        p2 = calc("p",1100,280,430,68,0,68)
        kd1 = calc("k",680,280,80,68,60,68)
        kd2 = calc("k",1640,280,80,68,60,70)


    elif size == [1117, 1600]:
        sc1 = calc(im,"s",700,140,90,60,0,0)
        sc2 = calc(im,"s",815,140,90,60,0,0)
        p1 = calc(im,"p",160,230,400,57,0,57)
        p2 = calc(im,"p",960,230,400,57,0,57)
        kd1 = calc(im,"k",565,230,65,57,50,57)
        kd2 = calc(im,"k",1365,230,65,57,50,57)


    elif size == [720, 1600]:
        sc1 = calc(im,"s",740,110,80,50,0,0)
        sc2 = calc(im,"s",850,110,80,50,0,0)
        p1 = calc(im,"p",150,180,350,45,0,45)
        p2 = calc(im,"p",990,180,350,45,0,45)
        kd1 = calc(im,"k",610,180,55,45,50,45)
        kd2 = calc(im,"k",1380,180,55,45,50,45)

       
    elif size == [1440, 1920]:
        sc1 = calc(im,"s",840,170,100,70,0,0)
        sc2 = calc(im,"s",980,170,100,70,0,0)
        p1 = calc(im,"p",190,280,430,68,0,68)
        p2 = calc(im,"p",1100,280,430,68,0,68)
        kd1 = calc(im,"k",680,280,80,68,60,68)
        kd2 = calc(im,"k",1640,280,80,68,60,70)

    elif size == [959, 1280]:
        sc1 = calc(im,"s",550,110,90,50,0,0)
        sc2 = calc(im,"s",650,110,90,50,0,0)
        p1 = calc(im,"p",130,185,300,45,0,45)
        p2 = calc(im,"p",750,185,300,45,0,45)
        kd1 = calc(im,"k",450,185,45,45,45,45)
        kd2 = calc(im,"k",1090,185,45,45,45,45)

    elif size == [1200, 1600]:
        sc1 = calc(im,"s",700,140,90,60,0,0)
        sc2 = calc(im,"s",815,140,90,60,0,0)
        p1 = calc(im,"p",160,230,400,68,0,68)
        p2 = calc(im,"p",960,230,400,68,0,68)
        kd1 = calc(im,"k",565,230,65,68,50,68)
        kd2 = calc(im,"k",1365,230,65,68,50,68)

    elif size == [1439, 1920]:
        sc1 = calc(im,"s",840,170,100,70,0,0)
        sc2 = calc(im,"s",980,170,100,70,0,0)
        p1 = calc(im,"p",190,280,430,68,0,68)
        p2 = calc(im,"p",1100,280,430,68,0,68)
        kd1 = calc(im,"k",680,280,80,68,60,68)
        kd2 = calc(im,"k",1640,280,80,68,60,70)

    elif size == [1919, 2560]:
        sc1 = calc(im,"s",1100,230,170,90,0,0)
        sc2 = calc(im,"s",1290,230,170,90,0,0)
        p1 = calc(im,"p",260,380,430,90,0,90)
        p2 = calc(im,"p",1530,380,430,90,0,90)
        kd1 = calc(im,"k",900,380,100,90,90,90)
        kd2 = calc(im,"k",2180,380,100,90,90,90)
    
    elif size == [1080, 2400]:
        sc1 = calc(im,"s",1050,220,150,80,0,0)
        sc2 = calc(im,"s",1220,220,150,80,0,0)
        p1 = calc(im,"p",160,350,500,85,0,85)
        p2 = calc(im,"p",1430,350,500,85,0,85)
        kd1 = calc(im,"k",850,350,80,85,80,85)
        kd2 = calc(im,"k",2050,350,80,85,80,85)


    else:
        sc1 = im[110:165,555:635]
        sc2 = im[110:165,645:735]
        p1 = [im[i:i+44,130:330] for i in range(190,410,44)]
        p2 = [im[i:i+44,770:940] for i in range(190,410,44)]
        kd1 = [[im[i:i+44,j:j+45] for j in range(450,630,45)] for i in range(190,410,44)]
        kd2 = [[im[i:i+44,j:j+45] for j in range(1090,1270,45)] for i in range(190,410,44)]
        

    return sc1,sc2,p1,p2,kd1,kd2




def calc(im,c,x,y,x1,y1,s_x=0,s_y=0):

    if c == "s":
        res = im[y:y+y1,x:+x+x1]
    elif c == "p":
        res = [im[(i*s_y)+y:y+y1+(i*s_y),x:x+x1] for i in range(5)]
    elif c == "k":
        res = [[im[(i*s_y)+y:y+y1+(i*s_y),x+(j*s_x):x+x1+(j*s_x)] for j in range(4)] for i in range(5)]
    return res


# for zi,i in enumerate(os.listdir("ph")):
# path = os.path.join("ph",i)
# path = "qwe.jpg"
# im = cv2.imread(path)
# width,high,_ = im.shape 
# print(width,high)
# sizer([width,high],im)
