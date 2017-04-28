# Create game - inventory. Import data (string) from CSV, add to list and then to dictionary. 
# Print inventory unordered, descending order or ascending order - depend on user. Export data to CSV. 

import csv

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
added_items = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    '''Count number of items'''
    number = 0
    for key, value in inventory.items():
        number += value

    print("Total number of items: ", number)


def add_to_inventory(inventory, added_items):
    '''Adds to the inventory dictionary a list of items and count amount.'''
    for item in added_items:
        for key, value in inventory.items():
            if item == key:
                inventory[key] = value + 1

        if item not in inventory.keys():
            inventory[item] = 1

    return inventory


def print_table(inventory, order=None):
    '''Print table with inventory items.
    3 options: unordered, descending order or ascending order. Depending on user input.'''
    result = 0
    for key in inventory.keys():
        if len(key) > result:
            result = len(key)

    width = 3 + result
    title1 = 'count'
    title2 = 'item name'
    print('Inventory:', '\n', title1.rjust(width), title2.rjust(width))
    print(2*width*'-')

    if order == ' ':
        for key, value in inventory.items():
            print(str(value).rjust(width), key.rjust(width))

    if order == 'count,desc':
        for word in sorted(inventory, key=inventory.get, reverse=True):
            print(str(inventory[word]).rjust(width), word.rjust(width))

    if order == 'count,asc':
        for word in sorted(inventory, key=inventory.get, reverse=False):
            print(str(inventory[word]).rjust(width), word.rjust(width))

    print(2*width*'-')
    display_inventory(inventory)


def import_inventory(inventory, filename='import_inventory.csv'):
    '''Import data from CSV file. Change one string to list with elements.'''
    with open(filename, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='|', quoting=csv.QUOTE_NONE)
        for row in reader:
            for item in row:
                new_list = item.split(',')

        add_to_inventory(inventory, new_list)


def export_inventory(inventory, filename='export_inventory.csv'):
    '''Export all inventory to new or default file. Change inventory from dictionary to long string separate comma'''
    export_string = ''
    for key, value in inventory.items():
        new_key = key + ','
        export_string += new_key * value
    export = export_string[:-1]

    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_NONE)
        writer.writerow([export])


def main():
    inv = add_to_inventory(inventory, added_items)
    import_inventory(inv)
    order = input('''
    Push space - unordered,
    write count,desc - descending order
    write count,asc - ascending order: ''')
    print_table(inv, order)
    export_inventory(inv)

if __name__ == '__main__':
    main()