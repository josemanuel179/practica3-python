import unittest
import pandas as pd
from pandas._testing import assert_frame_equal
from src.query import Query 

class TestQuery(unittest.TestCase):
  
  def test_create_consult(self):
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
  
    q1Query = q1.createQuery()  

    query_list = [[80,0,160,1,30,1,25450,1.8,140,1,0,5]]
    query = pd.DataFrame(query_list, 
                 columns = ['age','anaemia','cpk','diabetes','ejection_franction',
                 'high_blood_preasure','platelets','creatinine','sodium','sex',
                 'smoking','time'])

    assert_frame_equal(q1Query, query)
