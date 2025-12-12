import random

# Izgara boyutu ve engel sayısı
GRID_SIZE = 4
num_obstacles = GRID_SIZE

# Izgarayı oluştur (NxN), listeler ile yapılacak.
def create_grid(size):
    pass                  

# Izgarayı çiz
def print_grid(grid):
    pass

# karakteri (x,y) koordinatları alarak ızgaraya ekle
def place_object(grid, symbol, x, y):
    pass

# Hareket ettir ve durumu kontrol et (engele çarpma burada kontrol ediliyor, 
#   yapabiliyorsanız main fonksiyonu içinde de kontrol edebilirsiniz)
def move_character(grid, character, direction):
    pass


# Engelleri rastgele yerleştir (burada ister bu fonksiyonun içinde ister yardımcı bir fonksiyon ile 
#   engellerin karakterin hedefe gitmesini imkansız kılacak şekilde dizilmesini engellemeniz gerekiyor )
def place_random_obstacles(grid, num_obstacles):
    pass

'''  def helper_function()  '''


# Ana program
def main():
    grid = create_grid(GRID_SIZE)
    
    print("2D Simülasyon Oyununa Hoşgeldiniz!")
    print("Oyunun başında bir karakter seçeceksiniz.")
    print("Hedefe (H) ulaşmaya çalışın, engele (X) çarpmamaya dikkat edin.")
    print("Komutlar: hareket için: [ u / d / l / r etc.], çık")
    
    character = input("Lütfen bir karakter seçin (ör: K): ")
    place_object(grid, character, 0, 0)  # Karakteri başlangıç noktasına yerleştir
    place_object(grid, "H", GRID_SIZE - 1, GRID_SIZE - 1)  # Hedefi yerleştir
    place_random_obstacles(grid, GRID_SIZE)

# Programı çalıştır
main()




