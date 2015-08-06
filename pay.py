import sys

def get_hours():
  try:
    if sys.argv[3] !=0:
        return sys.argv[3]
  except:
    return 40

def calculate_hourly():
  hours = get_hours()
    
  salary = float(sys.argv[2])
  weekly = round(salary/52, 2)
  hourly = round(weekly/float(hours), 2)
  
  print 'For an annual salary of $' + str(salary) + ':'
  print 'Based on', hours, 'hours per week:'
  print 'Weekly pay is: $' + str(weekly) + ' per week and,'
  print 'Hourly pay is: $' + str(hourly) + ' per hour'

def calculate_salary():
  hours = get_hours()
  hourly = float(sys.argv[2])
  weekly = hourly * float(hours)
  salary = weekly * 52

  print 'At $' + str(hourly) + ' per hour, and ' + str(hours) + ' per week'
  print 'Yearly salary will be $' + str(salary)

try:
  if sys.argv[1].lower() == 's':
    try:
      float(sys.argv[2])
      calculate_hourly()
    except:
      print "usage: 'pay s floating_point_number'"
  elif sys.argv[1].lower() == 'h':
    try:
      float(sys.argv[2])
    except:
      print "usage: 'pay h floating_point_number'"
    calculate_salary()
except:
  print "usage: 'pay h floating_point_number'"
