import numpy as np
from voyager import Index, Space
import time

DIMENSIONS = 30

def get_item(index: int):
  return [i for i in range(index, index+DIMENSIONS)]

start = time.time()

index = Index(Space.Euclidean, num_dimensions=DIMENSIONS)
for i in range(1000):
  id = index.add_item(get_item(i))

neighbors, distances = index.query(get_item(10), k=10)
print("get neighbors of ", get_item(10))
for i, neighbor in enumerate(neighbors):
  distance = distances[i]
  print(i)
  print(" ", get_item(neighbor.astype(int)))
  print(" ", distances)


index.save("output_file.voy")

end = time.time()
print(end - start)
