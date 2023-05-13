# 这个函数用于登录用户
# 它接受一个请求对象，并返回一个JsonResponse对象
# 请求对象应包含一个JSON对象，其中包含用户的名称和密码
# 如果凭据正确，函数将对用户进行身份验证并登录
# 如果凭据不正确，它将返回错误消息

from django.http import JsonResponse
from utils.fbmsg import FBMsg
from django.contrib import auth
from django.contrib.auth.models import User
import json
from userprofile.models import Users
from staff.models import ListModel as staff


def login(request, *args, **kwargs):
    # 从请求对象中获取用户的名称和密码
    post_data = json.loads(request.body.decode())
    data = {
        "name": post_data.get('name'),
        "password": post_data.get('password'),
    }

    # 获取用户的IP地址
    ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
        'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')

    # 检查用户是否存在于数据库中
    if User.objects.filter(username=str(data['name'])).exists():
        # 验证用户
        user = auth.authenticate(username=str(data['name']), password=str(data['password']))

        # 如果用户的凭据不正确，则返回错误消息
        if user is None:
            err_ret = FBMsg.err_ret()
            err_ret['data'] = data
            return JsonResponse(err_ret)

        # 如果用户的凭据正确，则登录并返回其信息
        else:
            auth.login(request, user)
            user_detail = Users.objects.filter(user_id=user.id).first()
            staff_id = staff.objects.filter(openid=user_detail.openid, staff_name=str(user_detail.name)).first().id
            data = {
                "name": data['name'],
                'openid': user_detail.openid,
                "user_id": staff_id
            }
            ret = FBMsg.ret()
            ret['ip'] = ip
            ret['data'] = data
            return JsonResponse(ret)

    # 如果用户不存在于数据库中，则返回错误消息
    else:
        err_ret = FBMsg.err_ret()
        err_ret['ip'] = ip
        err_ret['data'] = data
        return JsonResponse(err_ret)


