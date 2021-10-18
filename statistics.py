
def calculateStats(numbers):
  computedStats = {}
  if numbers==[]:
    computedStats["avg"] = math.nan
    computedStats["max"] = math.nan
    computedStats["min"] = math.nan
  else:
    computedStats["avg"] = sum(numbers)/len(numbers)
    computedStats["max"] = max(numbers)
    computedStats["min"] = min(numbers)
  return computedStats
