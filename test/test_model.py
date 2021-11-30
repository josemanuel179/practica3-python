import unittest
import os
import pandas as pd
from src.model import ModelGenerator

class TestModelGenerator(unittest.TestCase):
  
  def test_create_model(self):
    model = ModelGenerator()
    model.createModel()
    self.assertTrue(model)

  def test_load_model(self):
    model = ModelGenerator()
    model.loadModel('modelo-pregenerado')
    self.assertTrue(model)
  
  def test_save_model(self):
    model = ModelGenerator()
    model.createModel()
    model.saveModel('modelo-test')
    self.assertTrue(os.path.isfile('models/modelo-test.sav'))
