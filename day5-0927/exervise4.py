# Write a function to print out the three timestable as a list(ending with 36). 

# Then modify your function to take a number as input and then print out its times table (ending with 12*number)


def three_time(num):
# three_times_table = []
   for i in range(1,13):
        st = ""
        value = i * num
        st = str(i)+" * "+str(num)+" = "+str(value)
        print(st)


three_time(2)