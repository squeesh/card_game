import pickle


def obj_to_string(obj):
    byte_data = pickle.dumps(obj)
    hex_string = hex(int.from_bytes(byte_data, byteorder='big'))
    return hex_string

def string_to_obj(string):
    int_data = int(string, 16)
    byte_data = int_data.to_bytes((int_data.bit_length() // 8), byteorder='big')
    return pickle.loads(byte_data)
