def seek(data, tag, index = 1):
    if isinstance(data, int) or isinstance(data, long) or isinstance(data, float) or isinstance(data, basestring):
        return None
    for entry in data:
        if entry == tag:
            index = index - 1
            if index <= 0:
                return data[entry]
        
        res = None
        if isinstance(entry, dict):
            res = seek(entry, tag, index)
        else:
            res = seek(data[entry], tag, index)
        if res != None:
            return res