def get_record_pos(n_line, n_column, _n_item):
    _n_item_base0 = _n_item - 1
    n_items_per_page = n_line * n_column
    _n_page = _n_item_base0 // n_items_per_page + 1

    _n_line = (_n_item_base0 % n_items_per_page) // n_column + 1

    _n_column = _n_item_base0 % n_column + 1

    return _n_page, _n_line, _n_column
