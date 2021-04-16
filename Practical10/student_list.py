class student(object):
    def list(self):
        print("%s %s %s" % (self.firstname, self.lastname, self.major))
Mark = student()
Mark.firstname = "Mark"
Mark.lastname = "Lawson"
Mark.major = "BMS"

Mark.list()