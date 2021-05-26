def non_empty(func):
    def wrapper():
        return list(filter(None, func()))
    return wrapper
@non_empty
def get_list():
    return ['chapter1', '', 'contents', '', 'line1']
print(get_list())