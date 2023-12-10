def min_vehicles(weights, max_limit):
    weights.sort(reverse=True)  
    vehicles = 0

    while weights:
        current_weight = weights.pop(0) 
        vehicles += 1

        for i in range(len(weights)):
            if current_weight + weights[i] <= max_limit:
                weights.pop(i)  
                break

    return vehicles


weights = list(map(int, input().split()))
max_limit = int(input())


result = min_vehicles(weights, max_limit)
print(result)
