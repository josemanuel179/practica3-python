import pandas as pd

class Query(object):

  def __init__(self):
    self._age = 0
    self._anemia = 0 
    self._cpk = 0
    self._diabetes = 0 
    self._ejectionFraction = 0
    self._highBloodPreasure = 0
    self._platelets = 0
    self._creatinine = 0
    self._sodium = 0
    self._sex = 0
    self._smoking = 0
    self._time = 0
  
  def createQuery(self):
    query_list = [[self.age, self.anemia, self.cpk, self.diabetes, self.ejectionFraction,
                  self.highBloodPreasure, self.platelets, self.creatinine, self.sodium,
                  self.sex, self.smoking, self.time]]
    
    columns_list = ['age','anaemia','cpk','diabetes','ejection_fraction',
                   'high_blood_pressure','platelets','creatinine','sodium','sex',
                   'smoking','time']

    query = pd.DataFrame(query_list, columns = columns_list)
    
    return query 

  # Get and Set --> Age
  def getAge(self):
    return self._age
       
  def setAge(self, age):
    self._age = age
  
  def delAge(self):
    del self._age
     
  age = property(getAge, setAge, delAge) 
  
  # Get and Set --> Anemia
  def getAnemia(self):
    return self._anemia
       
  def setAnemia(self, anemia):
    if anemia == True:
      self._anemia = 1
    elif anemia == False:
      self._anemia = 0

  def delAnemia(self):
    del self._anemia
     
  anemia = property(getAnemia, setAnemia, delAnemia) 
  
  # Get and Set --> CPK
  def getCPK(self):
    return self._cpk

  def setCPK(self, cpk):
    self._cpk = cpk
  
  def delCPK(self):
    del self._cpk
     
  cpk = property(getCPK, setCPK, delCPK) 
  
  # Get and Set --> Diabetes
  def getDiabetes(self):
    return self._diabetes

  def setDiabetes(self, diabetes):
    if diabetes == True:
      self._diabetes = 1
    elif diabetes == False:
      self._diabetes = 0
  
  def delDiabetes(self):
    del self._diabetes
     
  diabetes = property(getDiabetes, setDiabetes, delDiabetes) 

  # Get and Set --> EjectionFraction
  def getEjectionFraction(self):
    return self._ejectionFraction

  def setEjectionFraction(self, ejectionFraction):
    self._ejectionFraction = ejectionFraction
  
  def delEjectionFraction(self):
    del self._ejectionFraction
     
  ejectionFraction = property(getEjectionFraction, setEjectionFraction, delEjectionFraction) 

  # Get and Set --> HighBloodPreasure
  def getHighBloodPreasure(self):
    return self._highBloodPreasure

  def setHighBloodPreasure(self, highBloodPreasure):
    if highBloodPreasure == True:
      self._highBloodPreasure = 1 
    elif highBloodPreasure == False:
      self._highBloodPreasure = 0 
  
  def delHighBloodPreasure(self):
    del self._highBloodPreasure
     
  highBloodPreasure = property(getHighBloodPreasure, setHighBloodPreasure, delHighBloodPreasure) 

  # Get and Set --> Platelets
  def getPlatelets(self):
    return self._platelets

  def setPlatelets(self, platelets):
    self._platelets = platelets
  
  def delPlatelets(self):
    del self._platelets
     
  platelets = property(getPlatelets, setPlatelets, delPlatelets) 
  
  # Get and Set --> Creatinine
  def getCreatinine(self):
    return self._creatinine

  def setCreatinine(self, creatinine):
    self._creatinine = creatinine
  
  def delCreatinine(self):
    del self._creatinine
     
  creatinine = property(getCreatinine, setCreatinine, delCreatinine) 
  
  # Get and Set --> Sodium
  def getSodium(self):
    return self._sodium

  def setSodium(self, sodium):
    self._sodium = sodium
  
  def delSodium(self):
    del self._sodium
     
  sodium = property(getSodium, setSodium, delSodium) 
  
  # Get and Set --> Sex
  def getSex(self):
    return self._sex

  def setSex(self, sex):
    if sex == 'm' or 'male':
      self._sex = 1
    elif sex == 'f' or 'female':
      self._sex = 0
  
  def delSex(self):
    del self._sex
     
  sex = property(getSex, setSex, delSex) 
  
  # Get and Set --> Smoking
  def getSmoking(self):
    return self._smoking

  def setSmoking(self, smoking):
    if smoking == True:
      self._smoking = 1
    elif smoking == False:
      self._smoking = 0
  
  def delSmoking(self):
    del self._smoking
     
  smoking = property(getSmoking, setSmoking, delSmoking) 
  
  # Get and Set --> Time
  def getTime(self):
    return self._time

  def setTime(self, time):
    self._time = time
  
  def delTime(self):
    del self._time
     
  time = property(getTime, setTime, delTime) 
