def get_set_function_string():
    s = "\nvoid setPixel(int r,int g,int b,int addr)"
    s += "\n{"
    s += "\n\tSet_RGB_Params.Red=r;"
    s += "\n\tSet_RGB_Params.Green=g;"
    s += "\n\tSet_RGB_Params.Blue=b;"
    s += "\n\tdigLED_Set_RGB(Set_RGB_Params.Red, Set_RGB_Params.Green, Set_RGB_Params.Blue, addr, strip);"
    s += "\n\twait(1000);"
    s += "\n}"

    return s


def get_wait_function():
    s = "\nvoid wait(int d)"
    s += "\n{"
    s += "\n\tdelay(d);"
    s += "\n\tiseled_reset_counter++;"
    s += "\n\tif (iseled_reset_counter == 10000)"
    s += "\n\t\tiseled_reset();"
    s += "\n}"
    return s