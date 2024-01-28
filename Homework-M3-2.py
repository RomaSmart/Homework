import random

def get_numbers_ticket(min_number, max_number, quantity):    
  
    if not (1 <= min_number <= max_number <= 1000) or not (1 <= quantity <= (max_number - min_number + 1)):     # Перевірка введених даних
        return []
  
    unique_numbers = random.sample(range(min_number, max_number + 1), min(quantity, max_number - min_number + 1))    # Генеруємо випадковий набір унікальних чисел

    return unique_numbers   # Вертаємо список унікальних чисел

# При умові:
min_number = 1
max_number = 49
quantity = 6

result = get_numbers_ticket(min_number, max_number, quantity)
print(f"Випадкові числа від 1 до 49: {result}")