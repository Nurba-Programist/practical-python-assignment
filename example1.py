def draw_frame(width, height):
    # Проверяем, что ширина и высота больше 2
    if width < 2 or height < 2:
        print("Ширина и высота должны быть больше 2.")
        return

    # Строим верхнюю границу рамки
    print('-' * width)

    # Строим боковые границы
    for _ in range(height + 2):
       print('|' + ' ' * (width - 2) + '|')

    # Строим нижнюю границу рамки
    print('-' * width)

# Запрашиваем у пользователя ширину и высоту
try:
    user_width = int(input("Введите ширину рамки (минимум 2): "))
    user_height = int(input("Введите высоту рамки (минимум 2): "))
    
    draw_frame(user_width, user_height)
except ValueError:
    print("Пожалуйста, введите корректные целые числа.")