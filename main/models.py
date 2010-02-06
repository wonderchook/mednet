from django.db import models

# Create your models here.


def index(request):
    return render_to_response('index.html')

