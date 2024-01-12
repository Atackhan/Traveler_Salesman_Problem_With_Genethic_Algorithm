import random

# Şehirler arasındaki mesafeler matrisi
distances = [
    [0, 385, 300, 48, 550, 555, 885, 275, 1125, 1170],  # ordu
    [385, 0, 225, 470, 330, 210, 660, 175, 900, 800],  # yozgat
    [300, 225, 0, 280, 560, 435, 880, 220, 1120, 1100],  # sivas
    [48, 470, 280, 0, 600, 595, 930, 320, 1170, 1200],  # giresun
    [550, 330, 560, 600, 0, 220, 400, 370, 640, 790],  # karabük
    [555, 210, 435, 595, 220, 0, 445, 330, 690, 605],  # ankara
    [885, 660, 880, 930, 400, 445, 0, 970, 240, 670],  # istanbul
    [275, 175, 220, 320, 370, 330, 970, 0, 915, 945],  # amasya
    [1125, 900, 1120, 1170, 640, 690, 240, 915, 0, 730],  # edirne
    [1170, 800, 1100, 1200, 790, 605, 670, 945, 730, 0]  # muğla
]

# Kullanıcıdan veya rastgele oluşturulan rotaların giriş değerleri
def create_random_route():
    route = list(range(len(distances)))  # Tüm şehirleri içeren bir rota oluştur
    random.shuffle(route)  # Rotaları karıştır
    return route

def calculate_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        total_distance += distances[city1][city2]
    total_distance += distances[route[-1]][route[0]]  # Başlangıç şehrine geri dön
    return total_distance

def single_point_crossover(route1, route2):
    min_length = min(len(route1), len(route2))
    if min_length <= 2:
        return route1, route2
    crossover_point = random.randint(1, min_length - 1)
    new_route1 = route1[:crossover_point] + [city for city in route2 if city not in route1[:crossover_point]]
    new_route2 = route2[:crossover_point] + [city for city in route1 if city not in route2[:crossover_point]]
    return new_route1, new_route2

def validate_route(route):
    return len(set(route)) == len(distances) and route[0] == route[-1]

# Kullanıcıdan rotaları alır ve doğruluk kontrolü yapar
def get_user_routes():
    user_routes = []
    while len(user_routes) < 2:
        user_input = input(f"Lütfen {'ilk' if len(user_routes) == 0 else 'ikinci'} rotayı girin (0'dan başlayarak): ")
        user_route = list(map(int, user_input.split()))
        if validate_route(user_route):
            user_routes.append(user_route)
        else:
            print("Geçersiz rota. Lütfen her şehri bir kez ziyaret ettiğinizden ve başlangıç şehrine döndüğünüzden emin olun.")
    return user_routes

user_routes = get_user_routes()
random_routes = [create_random_route() for _ in range(2)]

initial_routes = user_routes + random_routes
initial_routes.sort(key=lambda x: calculate_distance(x))

best_routes = initial_routes[:2]

new_route1, new_route2 = single_point_crossover(best_routes[0], best_routes[1])
best_routes.extend([new_route1, new_route2])
best_routes.sort(key=lambda x: calculate_distance(x))

best_routes = best_routes[:2]

new_route3, new_route4 = single_point_crossover(best_routes[0], best_routes[1])
best_routes.extend([new_route3, new_route4])
best_routes.sort(key=lambda x: calculate_distance(x))

best_route = min(best_routes, key=lambda x: calculate_distance(x))

mutated_route = best_route.copy()
mutation_points = random.sample(range(len(mutated_route)), 2)
mutated_route[mutation_points[0]], mutated_route[mutation_points[1]] = mutated_route[mutation_points[1]], mutated_route[mutation_points[0]]

mutated_route_distance = calculate_distance(mutated_route)

print("Seçilen En İyi Rota:", best_route, "Mesafe:", calculate_distance(best_route))
print("Mutasyonsuz Rota:", mutated_route, "Mesafe:", mutated_route_distance)