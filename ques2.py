from weather import Weather

class forecast:
  weather = Weather()

  def temp(self):
   location = weather.lookup_by_location('halifax')
   condition = location.condition()
   print(condition['text'])

  for forecasts in location.forecast():
    print(forecasts['text'])
    print(forecasts['date'])
    print(forecasts['high'])
    print(forecasts['low'])
  def hightemp():
    for h in forecast('high'):
      if h > h+1:
        return h
      else:
       return h+1

  def lowtemp():
    for l in forecast('low'):
      if l > l+1: 
       return l+1
      else:
       return l

obj = forecast()
obj.find_forecast()

