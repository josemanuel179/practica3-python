import sys
import os
from query import Query
from model import ModelGenerator

def main():
  print('\n\nPráctica 3 Inteligencia Artficial')
  print('----------------------------------------')
  print('Manual [0]\tRealizar Consulta [1]\t\tSalir[2]')
  
  action = input()

  if action == '0':
    pass
  
  elif action == '1':
    modelMenu()

  elif action == '2':
    sys.exit('Finalizado programa...\n')
  
  else:
    print('Error. Consulta no válida')
    main()

def modelMenu():
  print('\nCrear nuevo modelo [0]\tUsar modelo existente [1]')
  
  action = input()

  if action == '0':
    queryMenu()

  elif action == '1':
    
    models = os.listdir('models')
    
    if models:
      print('\nLista de modelos existentes')
      print('----------------------------------------')
      for model in models:
        print(model)
    
    else:
      print('Error. No hay ningun modelo existente')
      modelMenu()

    model = input('\nModelo: ')
    
    queryMenu(model)

def queryMenu(modelFile):
  pass

def queryMenu():
  pass

if __name__ == '__main__':
  main()


'''
q1 = Query()
q1.setAge(80)
q1.setAnemia(False)
q1.setCPK(160)
q1.setDiabetes(True)
q1.setEjectionFraction(30)
q1.setHighBloodPreasure(True)
q1.setPlatelets(25450)
q1.setCreatinine(1.8)
q1.setSodium(140)
q1.setSex('male')
q1.setSmoking(False)
q1.setTime(5)

q1_query = q1.createQuery()
print(q1_query)

m1 = ModelGenerator()
m1.createModel()

result = m1.useModel(q1_query)
print(result)

m1.saveModel('modelo1')

m2 = ModelGenerator()
m2.loadModel('modelo1')
result2 = m1.useModel(q1_query)
print(result2)
print(m2.modelScore(0.9))
'''
