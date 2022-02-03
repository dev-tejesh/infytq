# Function to find permutations of a given string
# from itertools import permutations

# def allPermutations(str):
	
# 	# Get all permutations of string 'ABC'
# 	permList = permutations(str)

# 	# print all permutations
# 	for perm in list(permList):
# 		print (''.join(perm))
		
# # Driver program
# if __name__ == "__main__":
# 	str = 'ABC'
# 	allPermutations(str)
a=[1,2,2,3,4]
def even(x):
	return x%2==0
for item in a[:]:
	# if even(item):
		a.remove(item)
print(a)