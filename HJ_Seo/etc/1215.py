#### 추후 고민 후 꼭 풀어볼 것!!

# import time

import math
n,k = map(int,input().strip().split())

x = int(math.sqrt(k))

c = 0

if k<=n: # done.

    y = 0 
    z = 0

    for i in range(1,x+1):
        c += k//i * i
        c += ( (k//i + 1 + y) * (y - (k//i + 1) + 1) )//2 * z
        y = k//i
        z = i

    c += ( (y + z+1) * (y - (z+1) + 1) )//2 * z
    
elif x<n:
    
    y = 0 
    z = 0
    for i in range(1,x+1):
        c += k//i * i # 여기는 다 더해줘야함. 왜냐면 x<n이니까. 이후 값은?
        if n >= k//i:
            c += ( (k//i + 1 + y) * (y - (k//i + 1) + 1) )//2 * z
        y = min(k//i,n)
        z = i
    
    c += ( (y + z+1) * (y - (z+1) + 1) )//2 * z

else: # n <= x == sqrt(k) .. done
    for i in range(1,n+1):
        c += k//i*i

print(n*k - c)

#!  k<=n case에 대해서는 클리어, but n<k case에 대해 오답
# x = int(math.sqrt(k))

# c = 0
# y = 0 
# z = 0
# for i in range(1,x+1):
#     c += k//i * i
#     c += ( (k//i + 1 + y) * (y - (k//i + 1) + 1) )//2 * z # sum k//i + 1 ~ y  = ( (k//i + 1 + y) * (y - (k//i + 1) + 1) )//2
#     y = k//i
#     z = i

# c += ( (y + z+1) * (y - (z+1) + 1) )//2 * z

# print(n*k - c)



# start_time = time.time()  

# b = 0
# temp = 1  #시작점.
# for i in range(2,n+2):
#     if k//temp != k//i:
#         b += k//temp*(i-temp)*(temp+i-1)//2
#         # print(b,temp,i,n//temp)
#         temp = i
#  몫이 다른 i를 찾는 다른 방법은?

# print(n*k - b)
#! 시간초과. 다른 방법으로 나머지가 바뀌는 구간을 찾아야됨.
# rng = range(2,min(k//2+1,n+1))
# m = [k%i for i in rng]
# print(m)
# a = sum(m) # 이렇게 하는 경우 컴퓨터 메모리 초과... (10^8 10^8)
'''
yield를 이용해서 내부에 iter를 반환해주는 함수? 만들기.
첫 next = iter의 갯수, 이후 1만개 단위로 나눠묶어서 나머지sum?
두번째부터 sum(iter)

sum_(i=1)^(n) {k%i} =sum_(i=1)^(n) {k-(k//i)*i} = nk - sum_(i=1)^(n) {k//i*i}  

y = k/x..

k//(int(sqrt(k))+1) < int(sqrt(K)) ?..
15 기준.. (int(sqrt(k))+1) , k//(int(sqrt(k))+1) = 4 , 3
1 몫 15,  
1+1 몫 7 --> 15*(1)

2 몫 7,
2+1 몫 5 --> 7*(2)

3 몫 5,
3+1 몫 3 --> 5*(3)

4몫 3,
4+2 몫 2 --> 3*(4+5)

6 몫 2,
6+2 몫 1 --> 2*(6+7)

8 몫 1,
8+8 몫 0 --> 1*(sum_(i=8)^(8+7))

a~a+1 = a
a~b+1 = ((b-a+1)(b+a)/2) * (k//a) (a=b)가능.

15  1  15
7  2  14
5  3  15
/3  4  12
3  5  15
2  6  12
2  7  14
1  8  8
1  9  9
1  10  10
1  11  11
1  12  12
1  13  13
1  14  14
1  15  15
'''

# def lst_partition(iter,n,k):
#     leng = len(iter)
#     if leng%n == 0:
#         yield leng//n
#     else:
#         yield leng//n+1
#     a=0
#     while True:
#         b=0
#         c = a+n
#         if c>leng:
#             c = -1
#         for i in iter[a:c]:   #요거 어떻게 수정이 안되나???..,,,, -- 이게 수정되야함. 수정이 잘 될시 아래 if문의 숫자를 많이 줄여도 좋음.
#             b += k%i #lst와 sum을 적용시키는 것은 시간효율이 떨어짐.
#         a += n
#         yield b

# a = 0
# if min(k,n)>10000000:
#     iter = range(2,min(k//2+1,n+1))
#     x = lst_partition(iter,100000,k)

#     for i in range(next(x)): #1번식_new!.. 덧셈 분산을 해서 메모리를 조금 더 쓰고 시간을 약간 줄임(3/4정도, 10^8 10^8 기준.) but 작은 케이스에 대해서는 느림. 그런데 이것도 시간초과네??...,,,,ㅠㅠ
#         a += next(x)

# else:
#     for i in range(2,min(k//2+1,n+1)):  #1번식. i 가 k//2 보다 작을때는 나머지, i가 k//2보다 큰 경우 2번식과 3번식을 이용..
#         a += (k%i)
#         # k%i 를 재활용 할 수 있는 방법?

#     # print('a =',a)   #10 6일 때 0.

# '''
# k의 약수일 때 나머지는 0.
# k-1의 약수 i일 때 나머지는 항상 1%i.
# k-2의 약수 i일 때 나머지는 항상 2%i.
# ...
# k-x의 약수 i일 때 나머지는 항상 x%i
# ~~~ when i <= k//2., 자연스럽게 겹쳐지고 항상 잘 계산됨.

# --> 역산이 가능할까?? 별수없이 요걸 해야하네..,,,
# k%2
# k%3
# k%4
# k%5
# ...
# k%(k//2) == 1 or 0
# k%(k//2+1) == k//2 - 1
# ...
# k%(k-1)  == 1

# 19%15 = 4
# 19%5 = 4
# 19%3 = 1
# else?

# '''

# # a = 0
# # for i in range(2,min(k//2+1,n+1)):
# #     a += divmod(k,i)[1]   # 몫과 나머지 두개를 다 구하는 것이기 때문에 더 많은 시간이 걸림.


# mid_time = time.time()
# print(a)


# if k//2 < n: # 2번식. n이 k의 반 이상, 1 이하의 비율에 위치해 있을 때 n*n(+1)/2의 부분 식이 나옴.  따로 뺌.
#     col = max(k-k//2-1 + k-n, k-k//2) 
#     row = min(n - k//2, k-k//2-1)
#     # print('row & col =',row,col)
#     # print('col * row = ',col * row)  #10 6일 때 3.
#     a += col*row // 2

# if k <= n:
#     a += k*(n-k) #3번식. i가 k보다 큰 경우 나머지는 단순히 k, 이때 등호는 n-k로 인해 들어가도 가능.

# print(a)

# end_time = time.time()

# print('걸린 시간 =',end_time - start_time)
# print('걸린 시간 =',end_time - mid_time)

'''
1775329727317353 <-- input : 100000000 99999999
2416832290696316 <-- input : 99999999 999999998
2416832300935302 <-- input : 100000000 999999999
24168334560047 <-- input : 10000000 99999999
241684602728 <-- input : 1000000 9999999  ... 어떤 반복이 있다는 소리인데 ...
100000000 999999999
ex 10일때 
sum(
    10 - 1*10//1 = 10 - 10
    10 - 2*10//2 = 10 - 10
    10 - 3*10//3 = 10 - 9
    10 - 4*10//4 = 10 - 8
)

k, n ~= 3/4k.
 b = (k+1)//2 
 sum(b ~ k-n )

반 이상의 정수... k = (n-1)//2  sum = k*(k+1)/2
(ex 5/2 = 2.5.. 최소정수 = 3~4 --> 나머지는 차례대로 2 1)

약수, 서로소, (X) ... 11 --> 
5 => 1, 6 => 5

n = a + k*i for some k = n//i.
n = a-n//i = a - n//i + i+1 (mod i+1)

P(i) = a.
P(i+1) = P(i) - n//i if P(i)>=n//i

30%1 = 0
30%2 = 0 - 30 + (1+1) * 15 = 0
30%3 = 0 - 15 + 3*5 = 0
30%4 = 0 -10 + 4*3 = 2

...
30%10 = 0
30%(10+1) = 0 - 30//10 =  -3 + 10 + 1
30%(11+1) = 8 - 30//11 = 8 - 2 = 6
30%(12+1) = 6 - 30//12 = 6 - 2 = 4

10%3 = 1
10%7 = 3
10%9 = 1

10%4 = 2
10%6 = 4
10%8 = 2

1,2,5,10 = 0
2  --> (cycle(range(0)))..... 1 짜르고 2부터.
3  --> 
4  --> 0(cycle(range(1)))
5  --> 1
6  --> 0,0(cycle(range(2)))
7  --> 1,1
8  --> 0,2,0(cycle(range(3)))
9  --> 1,0,1
10 --> 0,1,2,0(cycle(range(4)))
11 --> 1,2,3,1 // 5,4,3,2,1,0 = 22
12 --> 0,0,0,2,0 // 5,4,3,2,1 = 17
13 --> 1,1,1,3,1 // 6,5,4,3,2,1 = 28
14 --> 0,2,2,4,2,0(cycle(range(6)))
15 --> 1,0,3,0,3,1

10 = 0,1,2,0,4  ,3
4  = 0,1,0,4,4  ,4
14 = 0,2,2,4,8-6,7-7.....

...
120 = 6! --> 0,0,0,0,0,1,0,3,0,10, ...

추가되는 cycle.. 
n == 2k, cycle(range(k-1)), last = 0
n == 2k+1, last = 1
0부터 k 미만의 숫자들.. 합은 k^2 미만.

ex) 8, cycle3을 따져보면 (8-6)%3
13 cycle5 --> (13-10)%5 = 3

a=0
for i in range(2,min(k//2+1,n+1)):
    a += (k-2*i)%i .... == k%i

n,k = 6,10
i = 1 --> 0
0
1
2
0
4 = 6

3
2
1
0

ex. 
301%4 = 3
301%6 = 1
301%3 = 1
301%2 = 1
'''

