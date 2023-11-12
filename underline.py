def underline(underlined:str, post:str='', pre:str=''):
    spaces = ' ' * len(pre)
    line = '¯' * len(underlined)
    return f'{pre}{underlined}{post}\n{spaces}{line}'