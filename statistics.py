
def calculateStats(numbers):
  computedStats = {}
  computedStats["avg"] = sum(numbers)/len(numbers)
  computedStats["max"] = max(numbers)
  computedStats["min"] = min(numbers)
  return computedStats
