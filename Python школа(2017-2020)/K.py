def my_int(c):
	return ord(c) - ord('0')

def Evaluate(s):	
	res = my_int(s[0])
	
	i = 1	
	while i < len(s):
		if s[i] == '+':
			res += my_int(s[i+1])
		elif s[i] == '-':
			res -= my_int(s[i+1])
		i += 2
	return res


s = input()

print(Evaluate(s))
