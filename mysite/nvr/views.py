from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from moviepy.editor import *
import json

# Create your views here.


def index(request):
    return HttpResponse(request.GET['message'])


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


default_path = "/temp/nvr/video"


def download(ip, duration, dowload_to_path:str = default_path)->str:
    """
    通过nvr下载摄像头视频
    :param ip: 摄像头ip
    :param duration:下载视频的时间段
    :param dowload_to_path: 下载视频的存放地址
    :return: 返回下载视频的绝对路径
    """
    pass


def concatenate(request):
    videos = []
    if not hasattr(request.POST, "data"):
        return HttpResponse(json.dumps({"status": "fail", "message": "请提供data字段值"}), content_type="application/json")
    try:
        data = json.loads(request.POST['data'])
        for ip, duration in data.items():
            videos.append(VideoFileClip(download(ip, duration, request.POST['path'] if "path" in request.POST else default_path)))

        final = concatenate_videoclips(videos, method="compose")
        final.write_videofile("final.mp4", audio=False)
        return HttpResponse(json.dumps({"status": "success", "message": "操作成功"}))
    except Exception as e:
        return HttpResponse(json.dumps({"status": "fail", "message": e}))




