i=1
def star(n):
	global i
	if i<=n:
		print(i,end=" ")
		i=i+1
		star(n)	
def main():
	print("Enter count")
	no=int(input())
	star(no)
if __name__=="__main__":
	main()

****************************output**************************
C:\Users\shree\Desktop\Python3\Assignments>python Assignment3_2.py
Enter count
5
1 2 3 4 5