def prime_number_list(n):
	for i in range(0,n):

		if i<=0:
			pass

		elif i==1:
			pass

		elif i%1==0:
			if i%i==0:
				for num in range(0,n):

					if i%num ==0:
						print (i)
					else:
						pass
			else: 
				pass

		else :
			pass

print(prime_number_list(10))
