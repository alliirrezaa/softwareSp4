from .serializers import OrderDetailSerializer
from rest_framework.response import Response
from rest_framework import status,viewsets,mixins,generics
from rest_framework.decorators import api_view
from ..models import OrderDetail
from rest_framework.generics import get_object_or_404

@api_view(['POST',])
def order_Detail(request):
    if request.method == 'POST':
        serializer=OrderDetailSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            form=serializer.save()
            data['response']='Successfully create a form.'
            return Response(data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class orderHitory(generics.ListAPIView):
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return OrderDetail.objects.filter(userId=self.request.user)