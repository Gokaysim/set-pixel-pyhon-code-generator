def get_frames_code(frames):

    changedPixels = "const changedPixel changedPixels[] = {"

    endOfFramePixelIndex = []

    animations_dict = frames[-1]
    frames = frames[:-1]

    index = 0
    for frame in frames:
        for addr in frame["addrs"]:
            changedPixels += "{(char)" + str(addr["r"]) + ", (char)" + str(addr["b"]) + ", (char)" + str(addr["g"]) + ", " + str(addr["addr"]) + "},"
            index += 1
        endOfFramePixelIndex.append(index)

    animations_str = 'const char included_animations[] = {'
    dict_length = len(animations_dict["animations"])

    for i in range(dict_length):
        for key in animations_dict:
            animations_str += '"' + str(animations_dict[key][i]) + '"' + ', '

    animations_str = animations_str[:-2]
    animations_str += '};'
    print(animations_str)

    changedPixels = changedPixels[:-1]    # to delete the comma at the end of the last pixel
    changedPixels += "};"

    endOfFramePixel = "const int endOfFramePixelIndex[] = {"
    for i in endOfFramePixelIndex:
        endOfFramePixel += str(i) + ", "

    endOfFramePixel = endOfFramePixel[:-2]    # to delete the comma after last frame's pixel index
    endOfFramePixel += "};"

    totalStr = "const int totalCount = " + str(index) + ";"

    animation_index = 0
    animation_pixel_change = 0  # number of digled set rgb commands per animation
    animation_location = 0  # for the values to be appended into animation_end list
    animation_end = []  # to store the endOfFramePixel value where animation ends
    print("Animations Number \t Number Of Changed Pixels")
    for frame in frames:
        if frame["new_animation"]:
            if animation_index == 0:
                animation_index += 1
                animation_pixel_change += len(frame["addrs"])
                animation_location += len(frame["addrs"])
            else:
                animation_end.append(animation_location)
                print("\t\t%d \t\t\t\t\t %d" % (animation_index, animation_pixel_change))
                animation_pixel_change = 0
                animation_index += 1
                animation_pixel_change += len(frame["addrs"])
                animation_location += len(frame["addrs"])
        else:
            animation_pixel_change += len(frame["addrs"])
            animation_location += len(frame["addrs"])
    animation_end.append(animation_location)
    print("\t\t%d \t\t\t\t\t %d" % (animation_index, animation_pixel_change))
    print(animation_end)

    animation_end_str = "const int animation_end_pixels[] = {"

    for end in range(len(animation_end)):
        animation_end_str += str(animation_end[end])
        animation_end_str += ", "
    animation_end_str = animation_end_str[:-2]
    animation_end_str += "};"
    # print(animation_end_str)

    return "\n" + changedPixels + "\n" + endOfFramePixel + "\n" + totalStr + "\n" + animations_str + "\n" + animation_end_str + "\n"
