# Вариант 7
import time
import os

class A:
    def __init__(self, val1, val2):
        self.rate_name = val1
        self.rate_price = val2

class B:
    def __init__(self):
        self.data = []

    def add_rate(self, name, price):
        os.system('clear')
        new_rate = (name, price)
        self.data.append(new_rate)
        
        print('Rate was added!\n')
        time.sleep(1)

    def find_min_rate_price(self):
        if not self.data:
            return None

        min_rate = min(self.data, key=lambda x: x[1])
        return min_rate
        
    def return_rate(self):
        if not self.data:
            return None

        return self.data

company = B()
os.system('clear')

while True:
    # Rate_menu
    print('\n----------Rate menu----------')
    print('1. Input Rate')
    print('2. Output min price of Rate')
    print('3. Output Rate data')
    print('4. Exit')
    print('-----------------------------')
    try:
        choice = int(input('Input: '))
        if choice == 1:
            try:
                name = input('Paste name rate: ')
                price = int(input('Paste rate price: '))
                company.add_rate(name, price)
            except ValueError:
                print(f'Price input must be number!!!') 

        elif choice == 2:
            os.system('clear')
            print('\nLoading...\n')
            time.sleep(1)

            res = company.find_min_rate_price()
            if res is None:
                print('Rate data is None\n')
            else:
                print(f'Min Rate price is...\nRate name / Rate price')
                print(f'{res[0]} / {res[1]}')

        elif choice == 3:
            os.system('clear')
            print('\nLoading...\n')
            time.sleep(1)

            rate_data = company.return_rate()
            if rate_data is None:
                print('Rate data is none')
            else:
                print('Rate name / Rate price')
                for rate_tuple in rate_data:
                    print(f'{rate_tuple[0]} / {rate_tuple[1]}')

        elif choice == 4:
            print('Exiting the program...')
            time.sleep(2)
            break

    except ValueError:
        print(f'Error: {ValueError}')

