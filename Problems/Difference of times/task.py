# put your python code here
hour_1 = int(input())
min_1 = int(input())
sec_1 = int(input())
hour_2 = int(input())
min_2 = int(input())
sec_2 = int(input())
hours = hour_2 - hour_1
minutes = min_2 - min_1
seconds = sec_2 - sec_1

sec_total = hours * 60 * 60 + minutes * 60 + seconds
print(sec_total)