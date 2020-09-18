from .models import Time_opt
import django_filters
 
 
class Time_optFilter(django_filters.FilterSet):
 
    class Meta:
        model = Time_opt
        fields = '__all__'