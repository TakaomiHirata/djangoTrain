from django.db import models

# Create your models here.
class Chara(models.Model,metaclass=models.base.ModelBase):
    name=models.CharField(max_length=20)
    hp=models.IntegerField()
    atk=models.IntegerField()
    matk=models.IntegerField()
    dif=models.IntegerField()
    mdif=models.IntegerField()
    spd=models.IntegerField()
    RARE_CHOICES=((3,3),(4,4),(5,5),)
    rare=models.IntegerField(choices=RARE_CHOICES,default=5)
    skill=models.IntegerField()
    JOB_CHOICES=((0,'戦士'),(1,'魔法使い'),(2,'ナイト'),
    (3,'僧侶'),(4,'アルケミスト'),)
    job=models.IntegerField(choices=JOB_CHOICES,default=1)
    
    def __init__(self,*args,**kwargs):
        models.Model.__init__(self,*args,**kwargs)
        self.nextBuf=0.0
        self.atkBuf=0.0
    def __str__(self):
        return self.name+str(self.rare)
    def calcAtk(self):
        return self.atk*self.skill*(1+self.nextBuf)*(1+self.atkBuf)/10000
    def calcMatk(self):
        return self.matk*self.skill*(1+self.nextBuf)*(1+self.atkBuf)/10000
    def calcDif(self):
        return self.dif*self.hp/10000
    def calcMdif(self):
        return self.mdif*self.hp/10000
    