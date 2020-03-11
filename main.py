from set_function import get_set_function_string,get_wait_function
from read_file import read_file
from get_frames_code import get_frames_code
from struct_generator import struct_generator


if __name__ == "__main__":

    p = get_wait_function()
    p += get_set_function_string()
    p += struct_generator()

    frames = read_file("./inova_logo.txt")

    p += get_frames_code(frames)

    p+="\nvoid main()"
    p+="\n{"
    p+="\n\tint nextEndFrame = endOfFramePixelIndex[0];"
    p+="\n\tint frameIndex = 0;"
    p+="\n\tfor(int i;i<totalCount;i++)"
    p+="\n\t{"
    p+="\n\t\tif(i == nextEndFrame)"
    p+="\n\t\t{"
    p+="\n\t\t\tframeIndex+=1;"
    p+="\n\t\t\tnextEndFrame=endOfFramePixelIndex[frameIndex];"
    p+="\n\t\t\twait(9999)"
    p+="\n\t\t}"
    p+="\n\t\tsetPixel((int)changedPixels[i].r,(int)changedPixels[i].g,(int)changedPixels[i].b,changedPixels[i].addr);"
    p+="\n\t}"
    p+="\n}"

    f = open("./program.c", "w")

    f.write(p)

    f.close()






