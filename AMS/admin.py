from django.contrib import admin

from .models import Demographic
from .models import BodyCompostion
from .models import FitnessTest
from .models import Wellness

admin.site.register(Demographic)
admin.site.register(BodyCompostion)
admin.site.register(FitnessTest)
admin.site.register(Wellness)
