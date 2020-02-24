from django.db.models import Q
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import CreateAPIView,DestroyAPIView,ListAPIView, UpdateAPIView,RetrieveAPIView,RetrieveUpdateAPIView

from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly

from firm.models import Employees
from .serializers import EmployeeCreateUpdateSerializer,EmployeeDetailSerializer,EmployeeListSerializer


class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeCreateUpdateSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EmployeeDetailAPIView(RetrieveAPIView):
    queryset = Employees.objects.all()
    lookup_field = 'slug'
    serializer_class = EmployeeDetailSerializer


class EmployeeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Employees.objects.all()
    lookup_field = 'slug'
    serializer_class = EmployeeCreateUpdateSerializer
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class EmployeeListAPIView(ListAPIView):
    serializer_class = EmployeeListSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    queryset = Employees.objects.all()
    search_fields = ['department', 'salary']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Employees.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(department__icontains=query)|
                    Q(salary__icontains=query)
                    ).distinct()
        return queryset_list