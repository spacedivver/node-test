import sys
sys.stdin = open("input.txt", "r")

t=int(input())
n,k=map(int,input().split())
arr=[[*map(int,input().split())] for _ in range(n)]
print(arr)