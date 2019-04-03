def weight_on_planets():
   weight = input('What do you weigh on earth? ')
   weight = int(weight)
   weightMars = weight * .38
   weightJupiter = weight * 2.34
   print('\nOn Mars you would weigh', weightMars, 'pounds.\nOn Jupiter you would weigh', weightJupiter, 'pounds.')
   # write your code here
   
   
   
if __name__ == '__main__':
   weight_on_planets()
