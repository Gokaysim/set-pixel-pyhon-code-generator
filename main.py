from set_function import get_set_function_string, get_wait_function, get_led_matrix
from read_file import read_file
from get_frames_code import get_frames_code
from struct_generator import struct_generator
from animation_distinguisher import get_animation

if __name__ == "__main__":

    frames = read_file("./input.txt")

    p = struct_generator()
    p += get_frames_code(frames)
    p += "\nint digled_ctr = 12; // 1 init_strip + 11 LUTs for proper white color\n"
    p += get_animation()
    p += get_wait_function()
    p += get_set_function_string()
    p += get_led_matrix()

    f = open("./program.c", "w")

    f.write(p)

    f.close()
