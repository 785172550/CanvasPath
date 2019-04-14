# coding:utf-8
# life is short, you need Python！
from .models import CustomUser

class EmailBackend(object):
    def authenticate(self, request, **credentials):
        # 要注意登录表单中用户输入的用户名或者邮箱的 field 名均为 username
        email = credentials.get('email', credentials.get('username'))
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            pass
        else:
            if user.check_password(credentials["password"]):
                return user

    def get_user(self, user_id):
        """
        该方法是必须的
        """
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
