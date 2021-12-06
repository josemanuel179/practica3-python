#!/bin/env python3

import sys
import argparse
import os
from src.query import Query
from src.model import ModelGenerator

def main():
  parser = argparse.ArgumentParser(description='Práctica 3 IA')
  parser.add_argument('-c', '--create-model', metavar='<nombre-modelo>', help='crear modelo nuevo')
  parser.add_argument('-l', '--load-model', metavar='<nombre-modelo>', help='cargar modelo')
  parser.add_argument('-q', '--new-query', help='generar nueva consulta', nargs='?', const=' ')
  parser.add_argument('-s', '--model-score', metavar='<tamaño-test>', help='calcular precisión modelo', nargs = '?', const=0.9)
  parser.add_argument('-g', '--graph', metavar= '', help='generar grafo', nargs = '?', const=' ')
  args = parser.parse_args()

  if args.create_model:
    model = ModelGenerator()
    model.createModel()
    model.saveModel(args.create_model)
    print(f"Modelo '{args.create_model}' generado\n")
  
  if args.load_model:
    model = ModelGenerator()
    model.loadModel(args.load_model)

  if args.new_query:
    q = Query()
    
    q.setAge(int(input('Edad [int]: ')))
    q.setAnemia(input('Anemia [s/n]: '))
    q.setCPK(int(input('CPK [int]: ')))
    q.setDiabetes(input('Diabetes [s/n]: '))
    q.setEjectionFraction(int(input('Fracción de eyección [int]: ')))
    q.setHighBloodPreasure(input('Presión arterial alta [s/n]: '))
    q.setPlatelets(float(input('Número de plaquetas [float]: ')))
    q.setCreatinine(float(input('Creatina [float]: ')))
    q.setSodium(float(input('Sodio [float]: ')))
    q.setSex(input('Sexo [hombre/mujer]: '))
    q.setSmoking(input('Fumador [s/n]: '))
    q.setTime(int(input('Tiempo en observación (horas) [int]: ')))

    query = q.createQuery()
    print('\nEl paciente ' + model.useModel(query) + '\n')

  if args.model_score:
    print(args.model_score)
    print(model.modelScore(float(args.model_score)))

  if args.graph:
    print(model.createGraph()) 

if __name__ == '__main__':
  main()
