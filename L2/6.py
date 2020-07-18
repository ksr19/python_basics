add_new_item = True
list_items = []
item_number = 0
while add_new_item:
    user_input = input("Вы хотите добавить новый товар? (y/n): ")
    if user_input.title() == "Y" or user_input.title() == "Yes":
        item_number += 1
        item_dict = {"название": None, "цена": None, "количество": None, "ед": None}
        item_tuple = (item_number, item_dict)
        item_dict["название"] = input("Введите название товара: ")
        item_dict["цена"] = float(input("Введите цену товара: "))
        item_dict["количество"] = int(input("Введите количество товара: "))
        item_dict["ед"] = input("Введите единицу измерения количества товара: ")
        list_items.append(item_tuple)
    else:
        add_new_item = False
print("Исходный список товаров: ", list_items)
print("Аналитика о товарах: ")
dict_items = {"название": None, "цена": None, "количество": None, "ед": None}
for item in list_items:
    item_dict = dict(list(item)[1])
    for key, value in item_dict.items():
        if dict_items[key] is None:
            dict_items[key] = [value]
        else:
            dict_items[key].append(value)
'''
Не совсем понял, как должны выглядеть набор значений "ед", если единица измерения хотя бы одного товара отличается.
Должны перечисляться все или все равно только уникальные? 
'''
if len(set(dict_items['ед'])) == 1:
    dict_items['ед'] = list(set(dict_items['ед']))
print(dict_items)
