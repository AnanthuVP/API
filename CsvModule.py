import csv
from os import write

# with open('stock_data.csv', 'r') as file:
#    reader = csv.Dictreader(file)
#    for row in reader:
#        print(row)


with open("output.csv", 'w') as file:
    writer = csv.writer(file, delimiter=':')
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Ananthu', 18, 'kannur'])
    writer.writerow(['Amaldev', 19, 'kasargod'])


with open("dictoutput.csv", 'w') as file:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Anuroop', 'age': 18, 'city': 'kannur'})
    writer.writerow({'name': 'Dingus', 'age': 22, 'city': 'kasargod'})

try:
    with open('STOCK.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except csv.Error as e:
    print(f'Error reading CSV file: {e}')
except FileNotFoundError as e:
    print(f'Not Such File is Found')
except Exception:
    print("Something went wrong")