from math import sqrt
from math import gcd
#promit:xây dựng cho tui hàm phân tích thành thừa số nguyên tố
#https://gemini.google.com/app/e72a268b6acb70d2
def KiemTraCoThePhanTichThanhSNT(n):
     i = 2
     while i*i <= n:
          while n % i == 0:
               n//= i 
               if n % i == 0:
                    return False
          i += 1
     return True

def IsPrime(n):
     if n < 2: return False
     for i in range(2,int(sqrt(n))):
          if n % i == 0:
               return False
     return True
def Primes():
     ans = []
     for i in range(int(sqrt(10**9))):
          if IsPrime(i):
               ans.append(i)
     return ans
def isSpecial(n):
     List_prime = Primes()
     i = 0
     while List_prime[i] * List_prime[i] <= n:
          while n % List_prime[i] == 0:
               n //= List_prime[i]
               if n % List_prime[i] == 0:
                    return False
          i+=1
     return True 
def TimSoCapKhoa(l,r):
     Special = []
     ans = 0
     for i in range(l,r+1):
          #if KiemTraCoThePhanTichThanhSNT(i):
          if isSpecial(i):
               Special.append(i)
     for i in range(len(Special)):
          for j in range(i+1,len(Special)):
               if gcd(Special[i],Special[j]) == 1:
                    ans+=1
     return ans

l,r = list(map(int,input().split()))
print(TimSoCapKhoa(l,r))

# fix phần phân tích thừa số nguyên tố, kiểm ra khi xét len() ko thay đổi