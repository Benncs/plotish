def check_in_dict(dic,name,default):
    if name in dic:
        val = dic[name]
    else:
        val=default
    return val