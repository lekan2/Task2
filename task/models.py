from djongo import models

class Person(models.Model):
    name = models.CharField(max_length=100, unique=True)
    

    def _str_(self):
        return f"{self.name}"
