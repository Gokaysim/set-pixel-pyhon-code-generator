def struct_generator():
    t = "\ntypedef struct changedPixel{"
    t += "\n\tchar r;"
    t += "\n\tchar b;"
    t += "\n\tchar g;"
    t += "\n\tshort addr;"
    t += "\n}changedPixel;\n"
    t += "\ntypedef struct animationTypes{"
    t += "\n\tshort animation_order;"
    t += "\n\tint animation_start_point;"
    t += "\n\tint animation_end_point;"
    t += "\n}animationTypes;\n"
    return t
