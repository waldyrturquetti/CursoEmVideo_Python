
count = s = 0 
while True:
	n = int(input('Digite um valor:'))
	if n == 999:
		break
	s += n
	count += 1

print(f'A soma dos {count} valores eh:{s}')
