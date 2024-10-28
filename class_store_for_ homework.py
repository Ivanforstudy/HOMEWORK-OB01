class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Курс '{item_name}' добавлен в университет'{self.name}' по цене {price}.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Курс '{item_name}' удален из университета '{self.name}'.")
        else:
            print(f"Курс '{item_name}' не найден в университете '{self.name}'.")

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Стоимость курса '{item_name}' обновлена до {new_price} в университете '{self.name}'.")
        else:
            print(f"Курс '{item_name}' не найден в университете '{self.name}'.")


store1 = Store("ZEROCODER", "https://zerocoder.ru/")

store2 = Store("ZEROCODER", "https://zerocoder.ru/")
store3 = Store("ZEROCODER", "https://zerocoder.ru/")

store1.add_item("Курс супердизайнеров", 1000000)
store1.add_item("Курс супертестировщиков", 1000000)

store2.add_item("Курс суперверсточников", 1000000)
store2.add_item("Курс суперкодеров", 1000000)


store3.add_item("Курс киберджедаев", 1000000)
store3.add_item("Курс кибергениев", 1000000)

print("\nТестирование курсов униерситета 'ZEROCODER':")
store2.add_item("ПРОМПТ Инженеров", 1000000)  # Добавление товара
print(f"Халява: {store2.get_item_price('Халява')}")  # Получение цены товара
store2.update_item_price("Халява", 0.8)  # Обновление цены товара
store2.remove_item("Благотворительность")  # Удаление товара
print(f"Цена Благотворительности после удаления: {store2.get_item_price('халява')}")  # Проверка цены удаленного товара
