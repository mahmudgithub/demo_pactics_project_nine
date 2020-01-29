from django.views.generic import ListView

from .models import Product
class One(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name='app1'



from .models import ProductImage
class One(ListView):
    model = ProductImage
    template_name = 'home.html'
    context_object_name='app1'


from .models import ProductTag
class One(ListView):
    model = ProductTag
    template_name = 'home.html'
    context_object_name='app1'


