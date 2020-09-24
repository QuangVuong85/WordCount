import base64
import json


def reduce(str_data):
    dict_data = {}
    str_decode64 = base64.b64decode(str_data)
    str_decode64 = str(str_decode64, "utf-8")
    listItem = str_decode64.split(";")
    for item in listItem:
        word, count = item.split(",")
        if word not in dict_data:
            dict_data[word] = 1
        else:
            dict_data[word] = dict_data[word] + int(count)
    result = json.dumps(dict_data)
    return result
