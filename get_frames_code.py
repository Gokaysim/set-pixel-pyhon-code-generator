

def get_frames_code(frames):

    changedPixels = "const changedPixel changedPixels[] ={"

    endOfFramePixelIndex =[]

    index =0
    for frame in frames:
        for addr in frame["addrs"]:
            changedPixels+="{(char)"+str(addr["r"])+",(char)"+str(addr["b"])+",(char)"+str(addr["g"])+","+str(addr["addr"])+"},"
            index+=1
        endOfFramePixelIndex.append(index)

    changedPixels+="};"

    endOfFramePixel = "const char endOfFramePixelIndex[] = {"
    for i in endOfFramePixelIndex:
        endOfFramePixel +=str(i)+",";

    endOfFramePixel +="};"

    totalStr = "const int totalCount =" + str(index) + ";";



    return "\n" + changedPixels +"\n"+ endOfFramePixel + "\n" + totalStr + "\n"
