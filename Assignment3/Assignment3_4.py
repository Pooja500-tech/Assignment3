s=0
i=0

def sum(n):
	global i
	global s
	if n>0:
		s=s+(n%10)
		n=n//10
		sum(n)
		return s
		
		
def main():
	print("Enter no")
	no=int(input())
	a=sum(no)
	print("addition is:",a)
if __name__=="__main__":
	main()

****************************output***************************
C:\Users\shree\Desktop\Python3\Assignments>python Assignment3_4.py
Enter no
123
addition is: 6