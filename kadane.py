#!/usr/env python
def kadane(arr):
	max_current = arr[0]
	max_global = arr[0]

	for i in arr[1:]:
		max_current = max(i, max_current+i)
		if max_current > max_global:
			max_global = max_current
		# print(i)
	return max_global


def main():
	print("Kadane algorithm..")
	lst = [-2,3,2,-1, -8, 990]
	print("The Maximum Subarray Sum of {}  = {}".format(lst, kadane(lst)))

if __name__ == '__main__':
	main()