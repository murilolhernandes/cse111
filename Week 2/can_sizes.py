import math

def main():
  best_can_storage = ""
  best_storage_efficiency = -1
  best_can_cost = ""
  best_cost_efficiency = -1
  can_names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5"]
  can_sizes = [(6.83, 10.16), (7.78, 11.91), (8.73, 11.59), (10.32, 11.91), (10.79, 17.78), (13.02, 14.29)]
  can_cost = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83]
  for name, can, cost in zip(can_names, can_sizes, can_cost):
    print(f"{name}: {compute_storage_efficiency(compute_volume(can[0], can[1]), compute_surface_area(can[0], can[1])):.2f} ${compute_cost_efficiency(compute_volume(can[0], can[1]), cost):.0f}")
    if compute_storage_efficiency(compute_volume(can[0], can[1]), compute_surface_area(can[0], can[1])) > best_storage_efficiency:
      best_storage_efficiency = compute_storage_efficiency(compute_volume(can[0], can[1]), compute_surface_area(can[0], can[1]))
      best_can_storage = name
    if compute_cost_efficiency(compute_volume(can[0], can[1]), cost) > best_cost_efficiency:
      best_cost_efficiency = compute_cost_efficiency(compute_volume(can[0], can[1]), cost)
      best_can_cost = name
  print(f"The best can for storage is {best_can_storage} with the volume efficiency of {best_storage_efficiency:.2f}")
  print(f"The best can for cost is {best_can_cost} with the cost efficiency of ${best_cost_efficiency:.0f}")

def compute_volume(radius, height):
  volume = math.pi * radius**2 * height
  return volume


def compute_surface_area(radius, height):
  surface_area = 2 * math.pi * radius * (radius + height)
  return surface_area

def compute_storage_efficiency(volume, surface_area):
  storage_efficiency = volume / surface_area
  return storage_efficiency

def compute_cost_efficiency(volume, cost_per_can):
  cost = volume / cost_per_can
  return cost

main()