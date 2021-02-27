f=1
def fact(n):
	if n>0:
		global f
		f=f*n
		fact(n-1)
		return f
		
def main():		
	print("Enter no")
	no=int(input())
	factorial=fact(no)
	print(factorial)

if __name__=="__main__":
	main()

*************************output*****************************
C:\Users\shree\Desktop\Python3\Assignments>python Assignment3_5.py
Enter no
5
120