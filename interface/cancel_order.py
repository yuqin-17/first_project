from common.sendmethod import SendMethod
from common.getkeyword import get_keyword

class Cancel_order:
    def __init__(self):
        self.url="http://ecshop.itsoso.cn/ECMobile/?url=/order/cancel"
    def cancel_order(self,data):
        return SendMethod.send_post(self.url,data=data)
    def cancel_order_is_success(self,cancel_order_id,new_order_ids):
        "判断删除的order_id是否还在未支付订单的order_ids中"
        if cancel_order_id in new_order_ids:
            return False
        else:
            return True


if __name__ == '__main__':
    from interface.login_interface import LoginInterface
    from interface.unpaid_order_interface import Unpaid_order_interface
    from common.getkeyword import get_keywords
    login = LoginInterface()
    import random
    login_data = {"name": "xiaohei666", "password": "123456"}
    session = login.get_session(data=login_data)
    print(session)
    data = {"session": session, "type": "await_pay", "pagination": {"count": 10, "page": 1}}
    unpaid = Unpaid_order_interface()
    print(unpaid.get_order_id(data=data))
    depids = unpaid.get_order_id(data=data)
    random_num = random.randint(0, len(depids))
    dep_id = depids[random_num]
    data={"session":session,"order_id":dep_id}
    print(Cancel_order().cancel_order_is_success(data))
