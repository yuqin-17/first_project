from common.sendmethod import SendMethod
from common.getkeyword import get_keyword

class To_be_shipped:
    def __init__(self):
        self.url="http://ecshop.itsoso.cn/ECMobile/?url=/order/list"
    def to_be_shipped(self,data):
        return SendMethod.send_post(self.url,data)
    def to_be_shipped_is_success(self,data):
        response=self.to_be_shipped(data)
        return get_keyword(response,"succeed")
if __name__ == '__main__':
    from interface.login_interface import LoginInterface

    login = LoginInterface()
    login_data = {"name": "xiaohei666", "password": "123456"}
    session = login.get_session(data=login_data)
    data = {"session":session,"type":"await_ship","pagination":{"count":10,"page":1}}
    print(To_be_shipped().to_be_shipped_is_success(data))