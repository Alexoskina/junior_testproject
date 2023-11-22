
def new_attribute(some_object, some_attribute):
    # Проверка наличие атрибута
    if hasattr(some_object, some_attribute):
        # Проверка, является ли атрибут числом
        if isinstance(getattr(some_object, some_attribute), (int, float)):
            # Увеличиваем значение атрибута на 1
            some_object.__dict__[some_attribute] += 1
            print(f"Значение атрибута {some_attribute} увеличено на 1.")
        else:
            print(f"Атрибут {some_attribute} не число.")
    else:
        print(f"Объект не имеет атрибута {some_attribute}.")

# Пример использования
class SomeObject:
    def __init__(self, some_attribute):
        self.some_attribute = some_attribute

obj = SomeObject(5)

# Увеличим значение атрибута на 1
new_attribute(obj, 'some_attribute')

# Увеличим значение несуществующего атрибута
new_attribute(obj, 'nonexistent_attribute')

# Увеличим значение нечисловогом атрибута
obj.some_attribute = "не число"
new_attribute(obj, 'some_attribute')