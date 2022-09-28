

from pprint import pprint
import cv2
import pytesseract
import numpy as np

from text import sizer
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'




def recognizer(name):
    im = cv2.imread(name)

    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    msk = cv2.inRange(hsv, np.array([0, 0, 120]), np.array([255, 255, 255]))

    krn = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
    dlt = cv2.dilate(msk, krn, iterations=1)
    im = 255 - cv2.bitwise_and(dlt, msk)
    width,high = im.shape
    # cv2.imshow("res",im)
    # cv2.waitKey(0)
    # print(im.shape)
    # return

    # cv2.rectangle(im,(450,190),(630,410),(250,0,0),2)
    # cv2.rectangle(im,(1090,190),(1270,410),(250,0,0),2)

    sc1,sc2,p1,p2,kd1,kd2 = sizer([width,high],im)
    

    config = r"--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789"
    p_config = r"--oem 3 --psm 6"
    

    sc1_res = pytesseract.image_to_string(sc1,config=config).strip() if pytesseract.image_to_string(sc1,config=config).strip() != "" else "0"
    sc2_res = pytesseract.image_to_string(sc2,config=config).strip() if pytesseract.image_to_string(sc2,config=config).strip() != "" else "0"
    p1_res = ["".join([x for x in pytesseract.image_to_string(i,config=p_config).strip().split("\n")[0].split() if len(x) > 2]) for i in p1]
    p2_res = ["".join([x for x in pytesseract.image_to_string(i,config=p_config).strip().split("\n")[0].split() if len(x) > 2]) for i in p2]
    kd1_res =[ [pytesseract.image_to_string(j,config=config).strip()[-2:] if pytesseract.image_to_string(j,config=config).strip()[-2:] != "" else '0' for j in i] for i in kd1]
    kd2_res =[ [pytesseract.image_to_string(j,config=config).strip()[-2:] if pytesseract.image_to_string(j,config=config).strip()[-2:] != "" else '0' for j in i] for i in kd2]

    finally_res = {
        "score":"",
        "c_ter":[],
        "ter":[]
    }
    finally_res["score"] = sc1_res + ":" + sc2_res
    for i,j in zip(p1_res,kd1_res):
        finally_res["c_ter"].append(
            {
                "name":i,
                "result":j
            }
        )
    for i,j in zip(p2_res,kd2_res):
        finally_res["ter"].append(
            {
                "name":i,
                "result":j
            }
        )
    return finally_res



                

          


def main():
    pprint(recognizer("1.jpg"))
    pprint(recognizer("qwe.jpg"))
    pprint(recognizer("ph/r8G8NRxuW9c.jpg"))



if __name__ == "__main__":
    main()


