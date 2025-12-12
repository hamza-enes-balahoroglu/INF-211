# ================================================================
# INF211 Project 2: 2D Simulation Game
# Student Name: Hamza Enes Balahoroğlu
# Student ID  : 240102002088
# ================================================================

import random
from enum import Enum, auto

class Status(Enum):
    CONTINUE_GAME   = auto()  # OYUNU_SURDUR
    HIT_OBSTACLE    = auto()  # ENGELE_CARPTI
    REACHED_TARGET  = auto()  # HEDEFE_ULASTI
    HIT_BOUNDARY    = auto()  # SINIRA_ULASTI
    INVALID_COMMAND = auto()  # TANIMSIZ_KOMUT

# Izgara boyutu ve engel sayısı
GRID_SIZE = 6
num_obstacles = GRID_SIZE
commands = {
#  command  : (y, x) 
    "u"     : (-1, 0),
    "d"     : (1 , 0),
    "r"     : (0 , 1),
    "l"     : (0 ,-1),
    "ul"    : (-1,-1),
    "ur"    : (-1, 1),
    "dl"    : (1 ,-1),
    "dr"    : (1 , 1),
    "çık"   : (0,  0),
}

# Izgarayı oluştur (NxN), listeler ile yapılacak.
def create_grid(size):
    grid = []
    
    for i in range(size):
        colm = []
        for j in range(size):
            colm.append("•")
            pass
        grid.append(colm)
        pass
    
    return grid                  

# Izgarayı çiz
def print_grid(grid):
    result = ""
    for i in grid:
        for j in i:
            result += str(j).center(3, " ")
            pass
        result += "\n"
        pass
    print(result)
    pass

# karakteri (x,y) koordinatları alarak ızgaraya ekle
def place_object(grid, symbol, x, y):
    grid[y][x] = symbol
    pass

# Hareket ettir ve durumu kontrol et (engele çarpma burada kontrol ediliyor, 
#   yapabiliyorsanız main fonksiyonu içinde de kontrol edebilirsiniz)
def move_character(grid, character, direction):
    
    if not direction in commands:
        direction = direction[::-1]
        if not direction in commands:
            print("Tanımsız Komut !")
            return Status.INVALID_COMMAND        
    
    x, y = index_of_character(grid, character)
         
    x_new = x + commands[direction][1]
    y_new = y + commands[direction][0]
    
    status = is_new_location_enable(grid, x_new, y_new)
    
    if status == Status.CONTINUE_GAME or status == Status.REACHED_TARGET:
        place_object(grid, "•", x, y)
        place_object(grid, character, x_new, y_new)
    elif status == Status.HIT_OBSTACLE:
        place_object(grid, "•", x, y)
        
    return status


# Engelleri rastgele yerleştir (burada ister bu fonksiyonun içinde ister yardımcı bir fonksiyon ile 
#   engellerin karakterin hedefe gitmesini imkansız kılacak şekilde dizilmesini engellemeniz gerekiyor )
def place_random_obstacles(grid, num_obstacles):
    
    obstacles = []
    while True:
        for i in range(num_obstacles):
            x = 0
            y = 0
            while not is_obstacl_enable(obstacles, x, y):
                x = random.randint(0, GRID_SIZE-1)
                y = random.randint(0, GRID_SIZE-1)
            obstacles.append((x, y))
        if is_path_possible(obstacles):
            break
        else:
            obstacles.clear()
        pass
    
    for x, y in obstacles:
        place_object(grid, "X", x, y)
    pass

'''  def helper_function()  '''
def is_target_found(x,y):
    if x == GRID_SIZE-1 and y == GRID_SIZE-1: 
        return Status.REACHED_TARGET
    else:
        return Status.CONTINUE_GAME

def index_of_character(grid, character):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == character:
                return (x, y)
    return (0, 0)

def is_new_location_enable(grid, x_new, y_new):
    if not (0<= x_new < GRID_SIZE and 0<= y_new < GRID_SIZE) :
        return Status.HIT_BOUNDARY
    
    elif grid[y_new][x_new] == "X":
        return Status.HIT_OBSTACLE
    
    else:
        return is_target_found(x_new, y_new)

def is_obstacl_enable(obstacles, x, y):
    for a , b in obstacles:
        if a == x and b == y:
            # iki engel aynı noktada olamaz
            return False

    
    if (x == 0 and y == 0)  or\
            (x == GRID_SIZE - 1 and\
             y == GRID_SIZE - 1 ):
        return False
    
    return True

def is_path_possible(obstacles):
        
    start_pos = (0, 0) # (x, y)
    target_pos = (GRID_SIZE - 1, GRID_SIZE - 1)
    
    travel = []
    checked = []

    travel.append(start_pos)
    checked.append(start_pos)

    while len(travel) > 0:
        
        current_x, current_y = travel.pop(0)
        
        if (current_x, current_y) == target_pos:
            return True  # Yol bulundu!

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
            next_x, next_y = current_x + dx, current_y + dy
            
            next_pos = (next_x, next_y)

            if 0 <= next_x < GRID_SIZE and 0 <= next_y < GRID_SIZE:
                
                if not (next_x, next_y) in obstacles:
                    
                    if next_pos not in checked:
                        checked.append(next_pos)
                        travel.append(next_pos)

    # while döngüsü bittiyse ve 'True' dönmediysek,
    # 'travel' listesi boşalmış demektir (gidilecek yer kalmadı).
    # Yani yol tıkalı.
    return False

# Ana program
def main():
    grid = create_grid(GRID_SIZE)
    
    print("2D Simülasyon Oyununa Hoşgeldiniz!")
    print("Oyunun başında bir karakter seçeceksiniz.")
    print("Hedefe (H) ulaşmaya çalışın, engele (X) çarpmamaya dikkat edin.")
    print("Komutlar: hareket için: [ u / d / l / r etc.], çık")    
    
    character = ""
    character = input("Lütfen bir karakter seçin (ör: K): ").strip()
    while character in ("H","X","•","x","") or len(character) != 1:
        character = input(
            "Karakter H, X veya • karakterlerinden biri veya boşluk karakteri olamaz ! \nTekrar Deneyin : "
            ).strip()
    
    
    place_object(grid, character, 0, 0)  # Karakteri başlangıç noktasına yerleştir
    place_object(grid, "H", GRID_SIZE - 1, GRID_SIZE - 1)  # Hedefi yerleştir
    place_random_obstacles(grid, GRID_SIZE)
    
    command = ""
    status = Status.CONTINUE_GAME
    while command != "çık":
        
        print_grid(grid)
        
        if status == Status.HIT_OBSTACLE:
            print("Engele Çarptınız Kaybettiniz.")
            break
        elif status == Status.REACHED_TARGET:
            print("Hedefe ulaştınız! Tebrikler, oyunu kazandırnız!")
            break
        
        command = input("Komut : ").lower()
        
        status = move_character(grid, character, command)
    else:
        print("Oyun Kapatılıyor. Teşekkürler !")
        

# Programı çalıştır
main()