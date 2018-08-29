from PIL import Image,ImageFont,ImageDraw
import random
import string

characters = string.ascii_letters+string.digits


def selectedCharacters(length):
    result = ""
    for i in range(length):
        result += random.choice(characters)
    return result

def getColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return(r,g,b)


def main(size,charactersNumber,bcgolor):
    imageTemp = Image.new('RGB',size,bcgolor)
    font = ImageFont.truetype('C:\\windows\\fonts\\TIMESBD.TTF',48)
    draw = ImageDraw.Draw(imageTemp)
    text = selectedCharacters(charactersNumber)
    print(text)
    width,height = draw.textsize(text,font)

    offset = 2
    for i in range(charactersNumber):
        offset += width//charactersNumber
        position = (offset,(size[1]-height)//2+random.randint(-10,10))
        draw.text(xy=position,text=text[i],font=font,fill= getColor())

    imageFinal = Image.new('RGB',size,bcgolor)
    pixelsFinal = imageFinal.load()
    pixelTemp = imageTemp.load()
    for y in range(0,size[1]):
        offset = random.randint(-1,1)
        for x in range(0,size[0]):
            newx = x + offset
            if newx >= size[0]:
                newx = size[0]-1
            elif newx<0:
                newx = 0
            pixelsFinal[newx,y] = pixelTemp[x,y]
    
    draw = ImageDraw.Draw(imageFinal)

    for i in range(int(size[0]*size[1]*0.07)):
        draw.point((random.randint(0,size[0]),random.randint(0,size[1])),fill=getColor())

    for i in range(8):
        start = (0,random.randint(0,size[1]-1))
        end = (size[0],random.randint(0,size[1]-1))
        draw.line([start,end],fill=getColor(),width=1)

    for i in range(8):
        imageFinal.save("result.jpg")
    imageFinal.show()


if __name__ == '__main__':
    main((300,100),8,(255,255,255))



