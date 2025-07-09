a = int(input())
t = int(input())
phase = int(input())

sum_0 = 0
sum_1 = 0
hum = -1

n = 2

def find(sum_0, sum_1, hum, n):
    while True:
        sen = [0, 1, 0, 1]
        sen_sum = [0]*n + [1]*n
        sen = sen+sen_sum
        # print(sen)
        n += 1
        for i in sen:
            hum += 1
            if hum == a:
                hum = 0
            if i == 0:
                sum_0 += 1
            else:
                sum_1 += 1
            if phase == 0:
                if sum_0 == t:
                    return hum
            else:
                if sum_1 == t:
                    return hum

result = find(sum_0, sum_1, hum, n)
print(result)
        