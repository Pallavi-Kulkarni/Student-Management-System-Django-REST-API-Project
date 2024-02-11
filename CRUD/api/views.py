from django.http import Http404
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer

class StudentView(APIView):

  def get(self,request,id=None):
    if id is not None:
      try:
        result=Students.objects.get(id=id)
        serializer=StudentSerializer(result)
        return Response({'status':'success','student':serializer.data},status.HTTP_200_OK)
      except Students.DoesNotExist:
        raise Http404("Student does not exist")
    else:
      result=Students.objects.all()
      serializer=StudentSerializer(result,many=True)
      return Response({'status':'success','students':serializer.data},status.HTTP_200_OK)
    
  
  def post(self,request):
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"status":"success","data":serializer.data},status.HTTP_200_OK)
    else:
      return Response({"status":"error","data":serializer.errors},status.HTTP_400_BAD_REQUEST)
    
    

  def patch(self,request,id):
    result=Students.objects.get(id=id)
    serializer=StudentSerializer(result,data=request.data,partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({'status':'success','data':serializer.data})
      
    else:
      return Response({'status':'error','data':serializer.errors},status.HTTP_400_BAD_REQUEST)
    

  def delete(self,request,id=None):
    result=get_object_or_404(Students,id=id)
    result.delete()
    return Response({'status':'success','data':"Record Deleted"})











    # import ipdb
    # ipdb.set_trace()