#Nakshatra Nitin Kawthale
#CS 175/501A
#average from input File with Exception Handling


def main():
    infile = None
    try:
        infile = open('numbers.txt', 'r')
        file_contents = infile.read()

        num_list = []
        total = 0
        count = 0
        print_value_error = False  

        lines = file_contents.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                continue  

            try:
                num = float(line)
            except ValueError as ve:
                if not print_value_error:  
                    print('ValueError occurred:', str(ve))
                    print_value_error = True
                continue  

            count += 1
            total += num
            num_list.append(num)
            if not print_value_error:
                print('I read in', count, 'number(s). Current number is:', num, 'Total is:', total)

        average = total / count if count > 0 else 0
        if not print_value_error:
            print('Average:', average)

    except IOError:
        print('An error occurred trying to read the file.')

    except Exception as e:
        print('An error occurred:', str(e))

    finally:
        if infile is not None:
            infile.close()

if __name__ == '__main__':
    main()


