def umbrella(weather):
  if weather.lower() == 'rain':
    return "Get that brolly girl"
  else: 
    return "Clear skies ahead"

print(umbrella('Sun'))
print(umbrella('Rain'))