import solve

run = True

while run:
	print('>>> ', end = '')
	res = input()

	if res == 'quit':
		run = False
		continue
		
	print(solve.solve(res))