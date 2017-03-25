def encrypt(plaintext,password):
	result = ""
	for i in range (len(plaintext)):
		shift = ord(password[i%len(password)]) - ord("a")
		res = ((ord(plaintext[i])-ord("A") + shift) % 26) + ord("A")
		result += chr(res)
	return result

print(encrypt("GOTEAM","azby"))


d = {1:2, 3:4, 5:6} 
d.update({"a":"b", 3:42})
print(d)

def rowSetMap(L):
	result = dict()

	for row in range(len(L)):
		for col in range(len(L[0]):
			digit = L[row][col]
