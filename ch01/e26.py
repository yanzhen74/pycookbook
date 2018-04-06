def get_record_pos(nLine, nColum, _nItem):

	_nItemBase0 = _nItem - 1
	nItemsPerPage = nLine * nColum
	_nPage = _nItemBase0 // nItemsPerPage + 1

	_nLine = (_nItemBase0 % nItemsPerPage) // nColum + 1

	_nColum = _nItemBase0 % nColum + 1

	return _nPage, _nLine, _nColum

