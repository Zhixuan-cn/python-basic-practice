 # Insert a new number into the sorted array
if __name__ == '__main__':
    a = [1,7,8,11,13,16,25,34,47,59,100,0]
    print ('original list:')
    for i in range(len(a)):
        print (a[i])
    number = int(input("\ninput a number:\n"))
    end = a[10]
    if number > end:
        a[11] = number
    else:
        for i in range(11):
            if a[i] > number:
                X = a[i]
                a[i] = number
                for j in range(i + 1,12):
                    Y = a[j]
                    a[j] = X
                    X = Y
                break
    print ('sorted list:')
    for i in range(12):
        print (a[i])


