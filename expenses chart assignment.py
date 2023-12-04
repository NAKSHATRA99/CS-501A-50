#Nakshatra Nitin Kawthale
#CS 175/501A
#expencespiechart



import matplotlib.pyplot as plt

def plot_pie_chart(labels, values):
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Expense Distribution')
    plt.show()

def main():
    try:
        with open('expenses.txt', 'r') as file:
            expenses = file.readlines()

        labels = []
        values = []

        for expense in expenses:
            try:
                label, value_str = expense.strip().split('\t')
                value = int(value_str)
                labels.append(label)
                values.append(value)
            except ValueError:
                print(f"Error converting value to integer in line: {expense}")

        if labels and values:
            plot_pie_chart(labels, values)
        else:
            print("No valid data to plot.")

    except IOError:
        print("Error reading the file. Make sure 'expenses.txt' exists.")

if __name__ == "__main__":
    main()
