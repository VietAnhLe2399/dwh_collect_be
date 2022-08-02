from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(('GET',))
def get_system_time(request):
    return Response({'status': 'OK', 'data': f'{datetime.now():%Y/%m/%d %H:%M:%S}'},
                    status=status.HTTP_200_OK)
