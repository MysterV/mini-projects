list1 = [1, 2, 6, 24, 29, 35, 43, 60, 76, 87, 152, 901]
query = 60


def search(start=0, end=len(list1)-1):
	mid = (start+end) // 2
	if list1[mid] == query: return mid
	elif end <= start: return
	elif list1[mid] > query: search(start, mid-1)
	elif list1[mid] < query: search(mid+1, end)


if mid := search(): print(f'found it, it is {list1[mid]} at index {mid}')
else: print('It is not here')