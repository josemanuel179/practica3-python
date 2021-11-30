#!/bin/env python3

import sys
import argparse
import os
from query import Query
from model import ModelGenerator

def main():
  parser = argparse.ArgumentParser(description='Práctica 3 IA')
  parser.add_argument('-c', '--create-model', metavar='', help='Crear modelo nuevo')
  parser.add_argument('-l', '--load-model', metavar='', help='Cargar modelo')
  parser.add_argument('-q', '--new-query', metavar='', help='Generar nueva consulta', 
      nargs = '?', const=' ') 
  args = parser.parse_args()

  if args.create_model:
    model = ModelGenerator()
    model.createModel()
    model.saveModel(args.create_model)
    print(f'Modelo {args.create_model} generado')
  
  if args.load_model:
    model = ModelGenerator()
    model.loadModel(args.load_model)

  if args.new_query:
    q = Query()
    
    q.setAge(int(input('Edad: ')))
    q.setAnemia(input('Anemia [s/n]: '))
    q.setCPK(int(input('CPK: ')))
    q.setDiabetes(input('Diabetes [s/n]: '))
    q.setEjectionFraction(int(input('Fracción de eyección: ')))
    q.setHighBloodPreasure(input('Presión arterial alta [s/n]: '))
    q.setPlatelets(int(input('Número de plaquetas: ')))
    q.setCreatinine(float(input('Creatina: ')))
    q.setSodium(float(input('Sodio: ')))
    q.setSex(input('Sexo [hombre/mujer]: '))
    q.setSmoking(input('Fumador [s/n]: '))
    q.setTime(int(input('Tiempo en observación (horas): ')))

    query = q.createQuery()
    print('\nEl paciente ' + model.useModel(query) + '\n')

if __name__ == '__main__':
  main()
