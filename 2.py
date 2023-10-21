from collections import defaultdict
from xml.dom.minidom import Childless


def get_num(char):
  if char == 'A':
    return 0
  elif char == 'B':
    return 1
  elif char == 'C':
    return 2

def main():
  S = list(input())
  N = len(S)
  child = 0
  parent = 1
  x = 0 # ?の出現回数
  
  dp = [[defaultdict(int) for j in range(3)] for i in range(N)]
  
  if S[0] == '?':
    dp[0][0]['A'] = 1
    dp[0][1]['B'] = 1
    dp[0][2]['C'] = 1
  elif S[0] == 'A':
    dp[0][0]['A'] = 1
  elif S[0] == 'B':
    dp[0][1]['B'] = 1
  elif S[0] == 'C':
    dp[0][2]['C'] = 1
    
  
  for s in S:
    if s == '?':
      x += 1

  for i in range(N-1):
    for j in range(3):
      for now_char, now_count in dp[i][j].items():
        if S[i+1] == 'A':
          dp[i+1][0]['A'] = dp[i+1][0]['A'] + now_count
        if S[i+1] == 'B':
          if now_char == 'A':
            dp[i+1][1]['AB'] = dp[i+1][1]['AB'] + now_count
          else:
            dp[i+1][1]['B'] = dp[i+1][1]['B'] + now_count
        if S[i+1] == 'C':
          if now_char == 'AB':
            dp[i+1][2]['C'] = dp[i+1][2]['C'] + now_count
            child += now_count
          else:
            dp[i+1][2]['C'] = dp[i+1][2]['C'] + now_count
        if S[i+1] == '?':
          dp[i+1][0]['A'] = dp[i+1][0]['A'] + now_count
          if now_char == 'A':
            dp[i+1][1]['AB'] = dp[i+1][1]['AB'] + now_count
          else:
            dp[i+1][1]['B'] = dp[i+1][1]['B'] + now_count
          if now_char == 'AB':
            dp[i+1][2]['C'] = dp[i+1][2]['C'] + now_count
            child += now_count
          else:
            dp[i+1][2]['C'] = dp[i+1][2]['C'] + now_count


  # for d in dp:
  #   print(d)
  parent = pow(3, x)
  print(child, parent)
  print(child / parent)


if __name__ == '__main__':
  main()