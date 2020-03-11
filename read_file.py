
def read_frame_line(line,new_animation):
    split_line =line.split()
    return {
        "frame_id": int(split_line[4]),
        "addrs":[],
        "new_animation":new_animation
    }

def read_set_rgb(line):
    split_line =line.split()

    return {
        "stripe":int(split_line[2]),
        "addr":int(split_line[4]),
        "r": round(int(split_line[6])/8),
        "g": round(int(split_line[8])/8),
        "b": round(int(split_line[10])/8),
    }

def read_set_rgb_with_contain_check(last_frame_pixels,line):
    obj = read_set_rgb(line)

    if len(last_frame_pixels) < obj["addr"]:
        last_frame_pixels.append(obj)
        return obj
    item = last_frame_pixels[obj["addr"]-1]

    if item is not None and (item["r"] != obj["r"] or item["g"] != obj["g"] or item["b"] != obj["b"]):
        last_frame_pixels[obj["addr"]-1] = obj
        return obj

    return None



def read_file(input_file_path):
    frames =[]

    input_file = open(input_file_path, 'r')

    # removes first line
    line = input_file.readline()

    frame = None
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

            temp_frame = read_frame_line(line,new_animation)
            if frame != None:
                frames.append(frame)
            frame = temp_frame
        elif line.startswith("set_rgb"):
            obj = read_set_rgb_with_contain_check(last_frame_pixels,line)
            if obj is not None:
                frame["addrs"].append(obj)
        else:
            raise Exception('Unknown line')

    # if file is empty, this if prevents exception
    if frame != None:
        # for appending the last iteration
        frames.append(frame)

    input_file.close()


    animation_index = 0
    animation_pixel_change = 0
    print("Animations Number \t Number Of Changed Pixels")
    for frame in frames:
        if(frame["new_animation"]):
            if(animation_index == 0):
                animation_index += 1
                animation_pixel_change += len(frame["addrs"])
            else:
                animation_pixel_change += len(frame["addrs"])
                print("%d \t %d"%(animation_index,animation_pixel_change))
                animation_index += 1
                animation_pixel_change = 0
        else:
            animation_pixel_change+=len(frame["addrs"])
    print("%d \t %d" % (animation_index, animation_pixel_change))
    # for frame_index in range(1,169,1):
    #     frame = {
    #         "addrs":[],
    #         "frame_id":frame_index
    #     }
    #     for addr in range(1,2101,1):
    #         frame["addrs"].append({
    #             "r": 10,
    #             "g": 44,
    #             "b": 123,
    #             "addr": addr,
    #         })
    #     frames.append(frame)

    # return format
    # [
    #   {
    #       "frame_id":1
    #       "addrs":[
    #           {
    #               "r":1,
    #               "g":1,
    #               "b":1,
    #               "addr":1
    #           }
    #       ]
    #   }
    # ]
    return frames
