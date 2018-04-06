def get_record_pos(n, c, x):
    npp = n * c
    _c = x % c
    p = int(x / npp) + 1
    p = p - 1 if x % npp == 0 else p
    _n = int((x - (p - 1) * npp) / c) + 1
    _n = _n - 1 if _c == 0 else _n
    _c = c if _c == 0 else _c
    #print(p, _n, _c, sep='-')
    return p, _n, _c


get_record_pos(5, 3, 16)
