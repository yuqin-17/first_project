from common.sendmethod import SendMethod
from common.getkeyword import get_keyword

class LoginInterface:
    def __init__(self):
        self.url="http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
    def login(self,data):
        """请求登录接口"""
        return SendMethod.send_post(self.url,data)

    def get_session(self,data):
        """获取登录后的session"""
        response=self.login(data)
        return get_keyword(response,"session")

if __name__ == '__main__':
    login = LoginInterface()
    login_data = {"name": "xiaohei666", "password": "123456"}
    session = login.get_session(data=login_data)
    print(session)
