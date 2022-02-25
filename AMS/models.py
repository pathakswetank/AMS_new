from django.db import models

class Demographic(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sports = models.CharField(max_length=30)
    gender_choice = (("M","Male"),("F","Female"))
    gender = models.CharField(max_length =1 , choices = gender_choice)
    phone = models.CharField(max_length = 10)
    email = models.EmailField(default = "swetank@cssbangalore.com")
    personal_record = models.CharField(max_length=200)
    date = models.DateTimeField('date')
    photo = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.first_name
    
class FitnessTest(models.Model):
    upper_limb_flexibility_right = models.IntegerField(default = 1)
    upper_limb_flexibility_left = models.IntegerField(default = 1)
    lower_limb_flexibility = models.IntegerField(default = 1)
    hand_grip_strength_right = models.IntegerField(default = 1)
    hand_grip_strength_left = models.IntegerField(default = 1)
    upper_limb_power = models.IntegerField(default = 1)
    lower_limb_power = models.IntegerField(default = 1)
    agility = models.IntegerField(default = 1)
    speed = models.IntegerField(default = 1)
    
    def __str__(self):
        return self.upper_limb_flexibility_right
    


class Wellness(models.Model):
    sleep_quality_choice = (("5","Very Good"),("4","Good"),("3","Fair"),("2","Poor"),("1","Very Poor"))
    mood_choice = (("5","Very Good"),("4","Good"),("3","Fair"),("2","Poor"),("1","Very Poor"))
    hydration_choice = (("5","Very Good"),("4","Good"),("3","Fair"),("2","Poor"),("1","Very Poor"))
    soreness_choice = (("5","No Soreness"),("4","Less"),("3","Mild"),("2","Moderate"),("1","Severe"))
    fatigue_choice = (("5","No fatigue"),("4","Less fatigue"),("3","Mild fatigue"),("2","Moderate fatigue"),("1","Severe fatigue"))
    rpe_choice = (("0","Rest"),("1","Really Easy"),("2","Easy"),("3","Moderate"),("4","Sort of Hard"),("5","Hard"),("6","Really Hard"),("7","Very Hard"),("8","Difficult"),("9","Maximal"))
    sleep_quality = models.CharField(max_length =1,choices = sleep_quality_choice,default = 1)
    hydration = models.CharField(max_length =1, choices = hydration_choice,default = 1)
    soreness = models.CharField(max_length =1, choices = soreness_choice,default = 1)
    rpe = models.CharField(max_length =1, choices = rpe_choice,default = 1)
    mood = models.CharField(max_length =1, choices = mood_choice,default = 1)
    fatigue = models.CharField(max_length =1, choices = fatigue_choice,default = 1)
    duration = models.IntegerField(default = 1)
    
    def __str__(self):
        return self.sleep_quality
    
        
class BodyCompostion(models.Model): 
    height = models.IntegerField('height in cm', default = 1)
    weight = models.IntegerField(default = 1)
    BMI = models.IntegerField(default = 1)
    fat_percentage = models.IntegerField(default = 1)
    lean_mass = models.IntegerField(default = 1)
    visceral_fat = models.IntegerField(default = 1)
    fat_free_mass = models.IntegerField(default = 1)
    water_contebt = models.IntegerField(default = 1)
    subcutaneou_fat = models.IntegerField(default = 1)
    
    def __str__(self):
        return self.height
    
    
    
    
