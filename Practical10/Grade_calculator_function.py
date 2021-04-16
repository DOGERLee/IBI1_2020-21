class Grades(object):
  def __init__(self, name, cp, pp, fe):
      self.__name = name
      self.__cp = cp
      self.__pp = pp
      self.__fe = fe

  def getGrade(self):
    Grade = 0.4 * self.__cp + 0.3 * self.__pp + 0.3 * self.__fe
    return round(Grade)
  def getName(self):
      return self.__name


grade1 = Grades("Mark", 90, 80, 60)
print(grade1.getName(), grade1.getGrade())