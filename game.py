class Player:
    def __init__(self, name, x, y):
        """
        Класс, представляющий игрока.

        Args:
            name (str): Имя игрока.
            x (int): Координата X игрока на карте.
            y (int): Координата Y игрока на карте.
        """
        self.name = name
        self.x = x
        self.y = y


class Enemy:
    def __init__(self, name, x, y):
        """
        Класс, представляющий врага.

        Args:
            name (str): Имя врага.
            x (int): Координата X врага на карте.
            y (int): Координата Y врага на карте.
        """
        self.name = name
        self.x = x
        self.y = y


class Map:
    def __init__(self, width, height):
        """
        Класс, представляющий карту.

        Args:
            width (int): Ширина карты.
            height (int): Высота карты.
        """
        self.width = width
        self.height = height

        self.tiles = [[None for _ in range(width)] for _ in range(height)]
        # Генерируем двумерный список, представляющий тайлы на карте


def start_battle():
    """
    Функция, вызываемая при начале битвы.
    """
    print("Началась битва! Вы встретили врага!")


def display_map(enemy, player, game_map):
    """
    Функция для отображения карты с игроком и врагом.

    Args:
        enemy (Enemy): Объект врага.
        player (Player): Объект игрока.
        game_map (Map): Объект карты.
    """
    is_battle = False  # Флаг для определения, началась ли битва
    for y in range(game_map.height):
        for x in range(game_map.width):
            if player.x == enemy.x and player.y == enemy.y and player.x == x and player.y == y:
                print("@", end=" ")  # Отображение игрока и врага на одной позиции
                is_battle = True
            elif player.x == x and player.y == y:
                print("P", end=" ")  # Отображение игрока
            elif enemy.x == x and enemy.y == y:
                print("E", end=" ")  # Отображение врага
            elif game_map.tiles[y][x] is None:
                print("-", end=" ")  # Отображение пустого тайла
            else:
                print("X", end=" ")  # Отображение других объектов на карте
        print()
    if is_battle:
        start_battle()


def move_player(player, dx, dy):
    """
    Функция для перемещения игрока на карте.

    Args:
        player (Player): Объект игрока.
        dx (int): Смещение по оси X.
        dy (int): Смещение по оси Y.
    """
    player.x += dx
    player.y += dy


def can_move(player, game_map, dx, dy):
    """
    Функция для проверки возможности перемещения игрока на карте.

    Args:
        player (Player): Объект игрока.
        game_map (Map): Объект карты.
        dx (int): Смещение по оси X.
        dy (int): Смещение по оси Y.

    Returns:
        bool: True, если игрок может переместиться, иначе False.
    """
    new_x = player.x + dx
    new_y = player.y + dy
    if new_x < 0 or new_x >= game_map.width or new_y < 0 or new_y >= game_map.height:
        return False  # Проверка выхода за пределы карты
    if game_map.tiles[new_y][new_x] is not None:
        return False  # Проверка наличия препятствия на новой позиции
    return True


def main():
    """
    Основная функция игры.
    """
    player = Player("Player", 0, 0)
    enemy = Enemy("Ork", 1, 1)
    game_map = Map(5, 5)

    while True:
        display_map(enemy, player, game_map)

        action = input("Введите действие (w - вверх, a - влево, s - вниз, d - вправо): ")
        if action == "w" and can_move(player, game_map, 0, -1):
            move_player(player, 0, -1)
        elif action == "a" and can_move(player, game_map, -1, 0):
            move_player(player, -1, 0)
        elif action == "s" and can_move(player, game_map, 0, 1):
            move_player(player, 0, 1)
        elif action == "d" and can_move(player, game_map, 1, 0):
            move_player(player, 1, 0)
        else:
            print("Недопустимое действие.")

        print()


if __name__ == "__main__":
    main()
