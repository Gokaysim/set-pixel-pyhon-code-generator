from set_function import get_set_function_string, get_wait_function
from read_file import read_file
from get_frames_code import get_frames_code
from struct_generator import struct_generator
from animation_distinguisher import get_animation

if __name__ == "__main__":

    frames = read_file("./input.txt")

    p = struct_generator()
    p += get_frames_code(frames)
    p += "int digled_ctr = 12; // 1 init_strip + 11 LUTs for proper white color\n"
    p += get_animation()
    p += get_wait_function()
    p += get_set_function_string()

    p += "\nvoid led_matrix()"
    p += "\n{"
    p += "\n\tint nextEndFrame = endOfFramePixelIndex[0];"
    p += "\n\tshort frameIndex = 0;"
    p += "\n\tshort frame_quantity = sizeof(endOfFramePixelIndex)/sizeof(endOfFramePixelIndex[0]);"
    p += "\n\tint EndAddrLastFrame = 0;"
    p += "\n\tshort animationIndex = 0;"
    p += "\n\tint delay_time = AnimationFrameDelay(0);\n"
    p += "\n\tfor(int j = 0; j < frame_quantity; j++)"
    p += "\n\t{"
    p += "\n\t\tdelay_time = AnimationFrameDelay(animationIndex);"
    p += "\n\t\tnextEndFrame = endOfFramePixelIndex[j];"
    p += "\n\n\t\tfor(int i = EndAddrLastFrame; i < endOfFramePixelIndex[j]; i+=2)"
    p += "\n\t\t{"
    p += "\n\t\t\tsetPixel((int)changedPixels[i].r, (int)changedPixels[i].g, (int)changedPixels[i].b, changedPixels[i].addr);"
    p += "\n\t\t}"
    p += "\n\t\tfor(int i = EndAddrLastFrame + 1; i < endOfFramePixelIndex[j]; i+=2)"
    p += "\n\t\t{"
    p += "\n\t\t\tsetPixel((int)changedPixels[i].r, (int)changedPixels[i].g, (int)changedPixels[i].b, changedPixels[i].addr);"
    p += "\n\t\t}"
    p += "\n\n\t\tif(endOfFramePixelIndex[j] == animation_end_pixels[animationIndex])"
    p += "\n\t\t{"
    p += "\n\t\t\twait(10000000);"
    p += "\n\t\t\tanimationIndex++;"
    p += "\n\t\t}"
    p += "\n\t\telse"
    p += "\n\t\t{"
    p += "\n\t\t\twait(delay_time);"
    p += "\n\t\t}"
    p += "\n\n\t\tEndAddrLastFrame = endOfFramePixelIndex[j];"
    p += "\n\t}"
    p += "\n\twait(50000000);"
    p += "\n}"

    f = open("./program.c", "w")

    f.write(p)

    f.close()
