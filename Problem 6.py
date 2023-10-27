inventory_data = {}

with open("inventory_table.txt", "r") as file:
    lines = file.readlines()
    
    for line in lines:
        parts = line.strip().split(": ")
        if len(parts) == 2:
            item_name, item_count = parts[0], parts[1]
            inventory_data[item_name] = len(item_count)
        else:
            item_name = parts[0]
            inventory_data[item_name] = 0

for item, count in inventory_data.items():

    print(f"{item}: {count}")
