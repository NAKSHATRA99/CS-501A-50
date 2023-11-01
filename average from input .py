#CS 175/501A
#Nakshatra Nitin Kawthale
# average from input

def main():
    infile = open('numbers.txt', 'r')
    file_contents = infile.read()
    infile.close()

    num_list = []
    total = 0
    count = 0

    lines = file_contents.split('\n')
    for line in lines:
        try:
            num = float(line.strip())
            count += 1
            total += num
            num_list.append(num)
            print('I read in', count, 'number(s). Current number is:', num, 'Total is:', total)
        except ValueError:
            pass

    average = total / count if count > 0 else 0
    print('Average:', average)

if __name__ == '__main__':
    main()
