class Students:

   def __init__(self, Name, Age, Class='Students'):
         self.Name = Name
         self.Age = Age
         self.Class = Class
   
   def avgScore(self, score1, score2, score3): 
         print(f"{self.Name} scored {(score1+score2+score3)//3}")

John = Students("John", 40, "AMS")
John.avgScore(55,88,42)