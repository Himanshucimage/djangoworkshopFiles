from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .models import lmsUser
from .serlializers import *

class LmsSignupUser(APIView):
    def post(self, request):
        serializer = LmsSignupUserSerializer(data=request.data)
        if serializer.is_valid():
            lmsUser.objects.create(**serializer.validated_data)
            return JsonResponse({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LmsGetUserDetail(APIView):
    def get(self, request):
        result = list(lmsUser.objects.values())
        return JsonResponse(result, status=status.HTTP_200_OK, safe=False)

class LmsUpdateEmail(APIView):
    def put(self, request):
        userdata = LmsUpdateEmailSER(data=request.data)
        if userdata.is_valid():
            email = userdata.data["email"]
            number = userdata.data["number"]
            lmsUser.objects.filter(number=number).update(email=email)
            message={"message":"email updated succesfully"}
            return JsonResponse(message, status=status.HTTP_201_CREATED)
        return JsonResponse(userdata.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LmsDeleteuser(APIView):
    def delete(self, request,number):
        lmsUser.objects.filter(number=number).delete()
        message={"message":"user deleted successfuly"}
        return JsonResponse(message, status=status.HTTP_204_NO_CONTENT)
        

        
        
