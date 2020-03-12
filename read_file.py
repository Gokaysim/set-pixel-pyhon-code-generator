def read_frame_line(line, new_animation):
    split_line = line.split()

    return {
        "frame_id": int(split_line[4]),
        "addrs": [],
        "new_animation": new_animation
    }


def read_animation_line(line):
    split_line = line.split()

    return {
        "animation_id": str(split_line[1])
    }


def read_set_rgb(line):
    split_line = line.split()

    return {
        "stripe": int(split_line[2]),
        "addr": int(split_line[4]),
        "r": round(int(split_line[6]) / 8),
        "g": round(int(split_line[8]) / 8),
        "b": round(int(split_line[10]) / 8),
    }


def read_set_rgb_with_contain_check(last_frame_pixels, line):
    obj = read_set_rgb(line)

    if len(last_frame_pixels) < obj["addr"]:
        last_frame_pixels.append(obj)
        return obj
    item = last_frame_pixels[obj["addr"] - 1]

    if item is not None and (item["r"] != obj["r"] or item["g"] != obj["g"] or item["b"] != obj["b"]):
        last_frame_pixels[obj["addr"] - 1] = obj
        return obj

    return None


def read_file(input_file_path):
    frames = []

    input_file = open(input_file_path, 'r')

    # removes first line
    line = input_file.readline()

    frame = None
    animation_dict = {
        'animations': []
    }

    last_frame_pixels = []
    # it assumes there are only 2 types of line
    while True:
        line = input_file.readline()
        if not line:
            break
        if line.startswith("frame_start"):
            new_animation = False
            if line.startswith("frame_start stripe: 0 frame: 0"):
                new_animation = True
            print(len(last_frame_pixels))
            print("new frame")
            # for the first iteration it will be None

            temp_frame = read_frame_line(line, new_animation)
            if frame is not None:
                frames.append(frame)
            frame = temp_frame
        elif line.startswith("set_rgb"):
            obj = read_set_rgb_with_contain_check(last_frame_pixels, line)
            if obj is not None:
                frame["addrs"].append(obj)
        elif line.startswith("animation:"):
            animations = read_animation_line(line)
            dict_new_val = animations["animation_id"]
            if dict_new_val != '':
                animation_dict["animations"].append(dict_new_val)
        else:
            raise Exception('Unknown line')

    # if file is empty, this if prevents exception
    if frame is not None:
        # for appending the last iteration
        frames.append(frame)

    input_file.close()

    print(animation_dict)
    frames.append(animation_dict)

    return frames
