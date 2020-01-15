from common.sendmethod import SendMethod
from common.getkeyword import get_keywords
from common.getkeyword import get_keyword



class Unpaid_order_interface:

    def __init__(self):
        self.url="http://ecshop.itsoso.cn/ECMobile/?url=/order/list"
    def unpaid_order(self,data):
        return SendMethod.send_post(url=self.url,data=data)
    def get_order_ids(self,data):

        response=self.unpaid_order(data=data)
        return get_keywords(response,"order_id")


    def unpaid_order_is_success(self,data):
        response=self.unpaid_order(data)
        return get_keyword(response,"succeed")

if __name__ == '__main__':
    from interface.login_interface import LoginInterface
    login = LoginInterface()
    import random
    login_data = {"name": "xiaohei666", "password": "123456"}
    session = login.get_session(data=login_data)
    print(session)
    data={"session":session,"type":"await_pay","pagination":{"count":10,"page":1}}
    unpaid=Unpaid_order_interface()
    print(unpaid.get_order_id(data=data))
    depids=unpaid.get_order_id(data=data)
    random_num=random.randint(0,len(depids))
    dep_id=depids[random_num]
    print(dep_id)

