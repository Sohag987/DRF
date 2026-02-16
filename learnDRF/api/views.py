'''
# using API view class 
from django.shortcuts import render
from .models import Course
from .serializers import CourseSerializers
from rest_framework.views import APIView

from rest_framework.response import Response 
from rest_framework import status



# Create your views here. 
class CourseModelView(APIView):

    def get(self,request,pk=None):
        if pk:
            try:
                course = Course.objects.get(pk=pk)
            except Course.DoesNotExist:
                return Response({'error':"Course Not Found"},status=status.HTTP_404_NOT_FOUND)
            
            serializer = CourseSerializers(course)
            return Response(serializer.data,status=status.HTTP_200_OK)
        

        course_all_data = Course.objects.all()
        serializer = CourseSerializers(course_all_data,many =True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = CourseSerializers(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED )
        
        else:
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk):
        if pk:
            try:
                course = Course.objects.get(pk=pk)
            except Course.DoesNotExist:
                return Response({'error':"Course does not exixt"},status=status.HTTP_404_NOT_FOUND)
            
            serializer = CourseSerializers(course,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
            
    def patch(self,request,pk):
        if pk:
            try:
                course = Course.objects.get(pk=pk)
            except Course.DoesNotExist:
                return Response({'error':"Course does not exixt"},status=status.HTTP_404_NOT_FOUND)
            
            serializer = CourseSerializers(course,data = request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self,request,pk):
        if pk:
            try:
                course = Course.objects.get(pk=pk)
            except Course.DoesNotExist:
                return Response({'error':"Course does not exixt"},status=status.HTTP_404_NOT_FOUND)
            
            course.delete()
          
            return Response({'msg':"Course deleted successfully"},status=status.HTTP_200_OK)
'''

'''
# Using Generic API view and Modelmixins 
from .serializers import CourseSerializers 
from .models import Course 
from rest_framework.generics import GenericAPIView 
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


class CourseListCreateviews(
    GenericAPIView,
    CreateModelMixin,ListModelMixin):

    queryset= Course.objects.all()
    serializer_class = CourseSerializers 

    def get(self,request,*args, **kwargs):
        return self.list(request,*args,**kwargs)
   
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args,**kwargs)
    
class Course_detailview(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
     queryset = Course.objects.all()
     serializer_class = CourseSerializers


     def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args,**kwargs)



    
     def put(self,request,*args, **kwargs):
        return self.update(request,*args,**kwargs)
    
     def patch(self,request,*args, **kwargs):
        return self.partial_update(request,*args,**kwargs)
    
     def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args,**kwargs)
'''
    

'''

# using  generiv views without mixins 
from .models import Course 
from .serializers import CourseSerializers 
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView 


class List_and_create(ListCreateAPIView):
    queryset = Course.objects.all() 
    serializer_class = CourseSerializers 


class retrieve_update_destroy(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    
'''
    

from .models import Course
from .serializers import CourseSerializers 
from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated


class course_curd(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers 
    permission_classes = [IsAuthenticated]



    


                

    


    


    
