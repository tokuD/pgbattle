from collections import defaultdict


def main():
  S = list(input())
  N = len(S)
  child = 0
  x = 0 # ?の出現回数
  
  dp = [defaultdict(int) for _ in range(N)]
  
  if S[0] == 'A':
    dp[0]['A'] = 1
  elif S[0] == '?':
    dp[0]['A'] = 1
    dp[0][''] = 2
  else:
    dp[0][''] = 2

  count = [0] * N
  for i in range(N):
    if S[i] == '?':
      x += 1
      if i == 0:
        count[0] = 1
      else:
        count[i] = count[i-1] + 1
    
  parent = pow(3, x)
  


  for i in range(N-1):
    for now_char, now_count in dp[i].items():
      if S[i+1] == 'A':
        dp[i+1]['A'] = dp[i+1]['A'] + now_count
        
      if S[i+1] == 'B':
        if now_char == 'A':
          dp[i+1]['AB'] = dp[i+1]['AB'] + now_count
        else:
          dp[i+1][''] = dp[i+1][''] + now_count
          
      if S[i+1] == 'C':
        dp[i+1][''] = dp[i+1][''] + now_count
        if now_char == 'AB':
          child += now_count * pow(3, x - count[i+1])
  
      if S[i+1] == '?':
        dp[i+1]['A'] = dp[i+1]['A'] + now_count
        
        if now_char == 'A':
          dp[i+1]['AB'] = dp[i+1]['AB'] + now_count
        else:
          dp[i+1][''] = dp[i+1][''] + now_count
        
        dp[i+1][''] = dp[i+1][''] + now_count
        if now_char == 'AB':
          child += now_count * pow(3, x - count[i+1])

  print(child, parent)
  print(child / parent)

if __name__ == '__main__':
  main()