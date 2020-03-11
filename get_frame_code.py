# TODO this value is delay count between frames, this value should be changed
frame_delay_amount = 999999

def get_frame_code(frame):
    s ="\n\t// new frame" + str(frame["frame_id"])


    for addr in frame["addrs"]:
        s+="\n\tsetPixel("+str(addr["r"])+","+str(addr["g"])+","+str(addr["b"])+","+str(addr["addr"])+");"
    s += "\n\twait("+str(frame_delay_amount)+");"
    return s