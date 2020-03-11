
def struct_generator():
    t = "\ntypedef struct changedPixel{"
    t += "\n\t char r;"
    t += "\n\t char b;"
    t += "\n\t char g;"
    t += "\n\t short addr;"
    t += "\n}changedPixel;\n\n"
    return t
