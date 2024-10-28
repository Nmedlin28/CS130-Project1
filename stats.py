import matplotlib.pyplot as plt
fhand = open("StudentExercise.csv")
next(fhand)
nums = []
for line in fhand:
    peices = line.split(',')
    hours = peices[0]
    if hours !='':
        hr = float(hours)
        nums.append(hr)
fig, ax = plt.subplots()
ax.hist(nums)
ax.set(xlabel = 'counts',
       title = 'How Many Times Each Word Appears')
plt.show()


       

def av_exercise(hours_list):
    if len(hours_list) == 0:
        return 0
    return sum(hours_list) / len(hours_list)

average = av_exercise(nums)




def prop_above(hours_list):
    avg = av_exercise(hours_list)
    over_avg = sum(1 for x in hours_list if x > avg)
    return over_avg / len(hours_list) if hours_list else 0



def median(hours_list):
    ls = sorted(hours_list)
    n = len(ls)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 0:
        return (ls[mid - 1] + ls[mid]) / 2
    else:
        return ls[mid]
    
    

print("Average = ", average)
print ("The Median hours of exercise is:", median(nums))
print ("Proportion of students above average =",prop_above(nums))




   

