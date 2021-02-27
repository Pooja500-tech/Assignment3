i=0
def star(n):
	global i
	if i<n:
		print(n,end=" ")
		n=n-1	
		star(n)
		
def main():
	print("Enter count")
	no=int(input())
	star(no)
if __name__=="__main__":
	main()

***************************output****************************
C:\Users\shree\Desktop\Python3\Assignments>python Assignment3_3.py
Enter count
5
5 4 3 2 1