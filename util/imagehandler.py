from PIL import Image
import requests

def overlayBubble(url):

    bubbleImage = Image.open("./assets/bubble.png").convert("RGBA")
    
    tempImage = Image.open(requests.get(url,stream=True).raw)
    addedHeight = heightTemp+heightBubble

    bubbled  = Image.new("RGBA",(widthTemp,addedHeight))

    bubbled.paste(tempImage,(0,heightBubble))
    bubbleImage = bubbleImage.resize((widthTemp,heightBubble))
    bubbled.paste(bubbleImage)
    return bubbled

