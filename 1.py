def main():
  N = int(input())
  A = list(map(int, input().split()))
  print(A)
  P = 1
  for a in A:
    P *= a

  ans = 0
  if P > 0:
    ans = '+'
  elif P < 0:
    ans = '-'

  print(ans)

if __name__ == '__main__':
  main()