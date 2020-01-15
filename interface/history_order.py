from common.sendmethod import SendMethod
from common.getkeyword import get_keyword
class History_order:
    def __init__(self):
        self.url="http://ecshop.itsoso.cn/ECMobile/?url=/order/list"
    def history_order(self,data):
        return SendMethod().send_post(self.url,data)
    def history_order_is_success(self,data):
        """判断是否成功"""
        response=self.history_order(data)
        return get_keyword(response,"succeed")
if __name__ == '__main__':
    from interface.login_interface import LoginInterface
    login = LoginInterface()
    login_data = {"name": "xiaohei666", "password": "123456"}
    session = login.get_session(data=login_data)
    data={"session":session,"type":"finished","pagination":{"count":10,"page":1}}
    print(History_order().history_order_is_success(data))
