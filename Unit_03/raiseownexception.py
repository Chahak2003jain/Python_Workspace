# raise your own exception

x= int(input("input x: "))

try:
	if x<0:
		raise Exception
		#print("x is : ",x)        dont write print statement here 
		
except Exception:
	print("YOU SHOULD NOT TAKE X NEGATIVE ")
	x= int(input("insert x: "))
	#print("x is : ",x)  		

else:
	print("x is : ",x)   # safe to write here If exception does Not occur 
finally:
	print("x is : ",x)

print("Hello world")
print("Hello world")	
print("Hello world")	
print("Hello world")	
print("Hello world")	
print("Hello world")	
print("Hello world")	
print("Hello world")	
print("Hello world")	

	
