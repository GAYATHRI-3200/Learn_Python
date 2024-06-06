#Sort a dictionary / dict comprehension
def sort_dict_by_key(d):
 return{k:d[k] for k in sorted(d)}
def sort_dict_by_value(d):
    return{k:v for k,v in sorted(d.items(), key=lambda x:x[1])}

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
print(sort_dict_by_key(d))
print(sort_dict_by_value(d))
