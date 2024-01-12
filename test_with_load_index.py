
from voyager import Index, Space
import time


start = time.time()

DIMENSIONS = 30

with open("output_file.voy", "rb") as f:
  index = Index.load(f)

neighbors, distances = index.query([j for j in range(DIMENSIONS)], k=DIMENSIONS)

for i, neighbor in enumerate(neighbors):
  distance = distances[i]
  print(i)
  print(" ", neighbor)
  print(" ", distances)

end = time.time()
print(end - start)

