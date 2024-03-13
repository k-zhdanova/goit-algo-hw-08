import heapq

def min_cost_to_connect_cables(cable_lengths):
    heapq.heapify(cable_lengths)
    total_cost = 0

    while len(cable_lengths) > 1:
        cost = heapq.heappop(cable_lengths) + heapq.heappop(cable_lengths)
        
        heapq.heappush(cable_lengths, cost)
        
        total_cost += cost

    return total_cost

cables = [8, 4, 6, 12]

min_cost = min_cost_to_connect_cables(cables)

print(f"Minimum cost to connect all cables: {min_cost}")