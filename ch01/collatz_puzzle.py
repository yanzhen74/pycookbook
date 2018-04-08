# Collatz puzzle has not solved from 1937


def get_collatz_list(_seed, _result):
    while _seed != 1:
        if _seed % 2 == 0:
            _seed //= 2
        else:
            _seed = _seed * 3 + 1
        _result.append(_seed)


seed = int(input('Give a seed:'))
result = [seed]
get_collatz_list(seed, result)
print("count is:", len(result))
print(result)
