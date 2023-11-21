def f_max(l):
    #когда пусто
    if not l:
        return None

    #если что-то есть
    if len(l) == 1:
        return l[0]

    max_r = f_max(l[1:])

    if max_r is None or l[0] > max_r:
        return l[0]
    else:
        return max_r
