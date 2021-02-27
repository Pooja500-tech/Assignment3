i=0
def star(n):
	global i
	if i<n:
		print("*",end=" ")
		i=i+1
		star(n)	
def main():
	print("Enter count")
	no=int(input())
	star(no)
if __name__=="__main__":
	main()
************************output***********************
C:\Users\shree\Desktop\Python3\Assignments>python Assignment3_1.py
Enter count
5
* * * * *
C:\Users\shree\Desktop\Python3\Assignments>
	