from time import time_ns
################################################
#naive implementation
def levenshtein(str1, str2, a, b):
  #if one string has ended, return the remaining length of the other string
  if a == 0: return b
  if b == 0: return a
  #if characters are equals, skip and make a recursive call.
  if str1[a-1] == str2[b-1]:
      return levenshtein(str1, str2, a-1, b-1)
  #if not equals
  return 1 + min(
    levenshtein(str1, str2, a, b-1),    #insert
    levenshtein(str1, str2, a-1, b),    #delete
    levenshtein(str1, str2, a-1, b-1)   #replace
  )
################################################
def levenshtein2(str1, str2, a, b):
  #create a 2D array with size axb
  dp = [[0] * (b+1) for x in range(a+1)]
  for i in range(a+1):
    for j in range(b+1):
      #if one string has ended, put the remaining length of the other string
      if i == 0: dp[i][j] = j
      elif j == 0: dp[i][j] = i
      #if characters are equals, put the previous value
      elif str1[i-1] == str2[j-1]:
        dp[i][j] = dp[i-1][j-1]
      #if not equals, find the minimum of the previous values of top, left, and diagonal
      else:
        dp[i][j] = 1 + min(
            dp[i][j-1],       #insert
            dp[i-1][j],       #remove
            dp[i-1][j-1]      #replace
        )
  return dp[a][b]
################################################
words = [
    "Good morning",
    "Good Bye",
    "Good boy",
    "Welcome",
    "Good evening",
    "Arab Academy",
    "Google",
]
query = input(">> ")
idx, dist = 0, 9999
start = time_ns()
for i, word in enumerate(words):
  d = levenshtein2(query, word, len(query), len(word))
  if d < dist:
    dist = d
    idx = i
print(f"You Query ({query}) match ({words[idx]}) by distance {dist}")
print(f"Elapsed: {(time_ns() - start) / 10e3} usec")
