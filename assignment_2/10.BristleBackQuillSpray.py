def CalculateTotalDamage(skil_laund_time,BaseDamage,BounsDamage,TimeExists):
     TotalDamage = 0
     TotalDamage += BaseDamage * len(skil_laund_time)
     TotalDamage += BounsDamage * (len(skil_laund_time) * (len(skil_laund_time) - 1) / 2)
     i = len(skil_laund_time) - 1
     while skil_laund_time[i] - TimeExists >= skil_laund_time[0]:
          count = 0
          # for x in skil_laund_time:
          #      if x < skil_laund_time[i] - TimeExists:
          #           count+=1
          #      else:
          #           break 
          for j in range(i-1,-1,-1):
               if skil_laund_time[j] < skil_laund_time[i] - TimeExists:
                    count = j + 1
                    break
          TotalDamage -= count*BounsDamage
          i-=1
     return int(TotalDamage)


if __name__ == '__main__':
     n = int(input())
     skill_laund_time = list(map(float,input().split()))
     BaseDamage = int(input())
     BounsDamge = int(input())
     TimeExists = float(input())

     print(CalculateTotalDamage(skill_laund_time,BaseDamage,BounsDamge,TimeExists))