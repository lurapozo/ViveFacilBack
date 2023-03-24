import sys
sys.path.append('/home/tomesoft1/TomeSoft_1/')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TomeSoft_1.settings")

import django
django.setup()

from api.models import PlanProveedor
from django.utils import timezone
from api.serializers import PlanProveedorSerializer

planesProveedor = PlanProveedor.objects.filter(fecha_expiracion__lt = timezone.now(), estado=True)
request = {"estado": False}
for i in planesProveedor:
    serializer = PlanProveedorSerializer(i, data=request, partial=True)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data, flush=True)