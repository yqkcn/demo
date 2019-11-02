from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework.viewsets import ViewSet
from django.http import response

def normal(request):
    """ 返回正常结果 """
    return response.HttpResponse('Hello World!')


def abnormal(request):
    """ 抛出普通异常 """
    raise ValidationError('Bad World!!!')


