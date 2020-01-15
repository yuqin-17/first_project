import unittest
import random
from common.getkeyword import get_keywords
from interface.login_interface import LoginInterface
from interface.history_order import History_order
from interface.to_be_received import To_be_received
from interface.to_be_shipped import To_be_shipped
from interface.unpaid_order_interface import Unpaid_order_interface
from interface.cancel_order import Cancel_order
from interface.pay_order import Pay_order
from common.database import Database
class Test_order(unittest.TestCase):
    def setUp(self):
        """登录"""
        self.login_data= {"name": "xiaohei666", "password": "123456"}
        return LoginInterface().get_session(self.login_data)

    def test_01_show_history_order(self):
        """查看历史订单"""
        data={"session":self.setUp(),"type":"finished","pagination":{"count":10,"page":1}}
        response=History_order().history_order(data)

        "断言"
        result=History_order().history_order_is_success(data)
        self.assertEqual(result,1)


    def test_02_show_unreceived_order(self):
        """查看未收货订单"""
        data={"session":self.setUp(),"type":"shipped","pagination":{"count":10,"page":1}}
        response=To_be_received().to_be_received(data)
        unreceived_ids=get_keywords(response,"order_id")
        print(unreceived_ids)
        """连接数据库"""
        database = Database(host="ecshop.itsoso.cn", user="ecshop", password="ecshop", database="ecshop",
                            charset='utf8', port=3306)
        sql = "select * from ecs_order_info where user_id=11402 and shipping_status=1"
        order_id_db = database.readall(sql=sql)
        # print(order_id_db)
        """在数据库中获取未收货的id"""
        db_orderid = get_keywords(order_id_db, "order_id")
        # print(db_orderid)
        """断言"""
        """判断未收货的id是否存在于数据库取消订单的id中"""
        for unreceived_id in unreceived_ids:
            if unreceived_id in db_orderid:
                self.assertTrue(True)
            else:
                self.assertTrue(False)



    def test_03_show_unshipped_order(self):
        """查看未发货订单"""
        data={"session":self.setUp(),"type":"await_ship","pagination":{"count":10,"page":1}}
        response=To_be_shipped().to_be_shipped(data)
        unship_order_ids=get_keywords(response,"order_id")
        print(unship_order_ids)
        """连接数据库"""
        database = Database(host="ecshop.itsoso.cn", user="ecshop", password="ecshop", database="ecshop",
                            charset='utf8', port=3306)
        sql = "select * from ecs_order_info where user_id=11402 and shipping_status=0"
        order_id_db = database.readall(sql=sql)
        print(order_id_db)
        """在数据库中获取取消订单的id"""
        db_orderid = get_keywords(order_id_db, "order_id")
        print(db_orderid)
        """断言"""
        """判断未发货的id是否存在于数据库取消订单的id中"""
        if unship_order_ids:
            for unship_order_id in unship_order_ids:
                if unship_order_id in db_orderid:
                    self.assertTrue(True)
                else:
                    self.assertTrue(False)
        else:
            print("未发货订单为零")


    def test_04_show_unpaid_order(self):
        """查看未支付订单"""
        data={"session":self.setUp(),"type":"await_pay","pagination":{"count":10,"page":1}}
        order_ids=Unpaid_order_interface().get_order_ids(data)
        print(order_ids)
        """连接数据库"""
        database=Database(host="ecshop.itsoso.cn",user="ecshop",password="ecshop",database="ecshop",charset='utf8',port=3306)
        sql="select * from ecs_order_info where user_id=11402 and pay_status=0"
        order_id_db=database.readall(sql=sql)
        print(order_id_db)
        db_orderids=get_keywords(order_id_db,"order_id")
        print(db_orderids)
        """断言"""
        for order_id in order_ids:
            if order_id in db_orderids:
                self.assertTrue(True)
            else:
                self.assertTrue(False)


    def test_05_cancel_order(self):
        """取消订单"""

        unpaid_data = {"session": self.setUp(), "type": "await_pay", "pagination": {"count": 10, "page": 1}}
        "获取未支付订单中的order_id"
        order_ids=Unpaid_order_interface().get_order_ids(unpaid_data)
        "随机获取一个order_id"
        random_num=random.randint(0,len(order_ids)-1)
        cancel_order_id=order_ids[random_num]
        print(cancel_order_id)
        "把随机获取的order_id传入cancel_data中"
        cancel_data={"session":self.setUp(),"order_id":cancel_order_id}
        "删除订单"
        Cancel_order().cancel_order(cancel_data)
        """连接数据库"""
        database = Database(host="ecshop.itsoso.cn", user="ecshop", password="ecshop", database="ecshop",
                            charset='utf8', port=3306)
        sql = "select * from ecs_order_info where user_id=11402 and order_status=3"
        order_id_db = database.readall(sql=sql)
        print(order_id_db)
        """在数据库中获取取消订单的id"""
        db_orderid = get_keywords(order_id_db, "order_id")
        print(db_orderid)
        """断言"""
        """判断取消订单的id是否存在于数据库取消订单的id中"""
        if order_id_db:
            if cancel_order_id in db_orderid:
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        else:
            print("数据库中订单状态被取消的订单为零")


    def test_06_pay_order(self):
        """支付订单"""
        "先查看未支付订单"
        unpaid_data = {"session": self.setUp(), "type": "await_pay", "pagination": {"count": 10, "page": 1}}
        "获取未支付订单中的order_id"
        order_ids = Unpaid_order_interface().get_order_ids(unpaid_data)
        "随机获取一个order_id"
        random_num = random.randint(0, len(order_ids)-1)
        print(random_num)
        pay_order_id = order_ids[random_num]
        print(pay_order_id)
        "把随机获取的order_id传入pay_data中"
        pay_data={"session":self.setUp(),"order_id":pay_order_id}
        "支付订单"
        Pay_order().pay_order(pay_data)
        """连接数据库"""
        database = Database(host="ecshop.itsoso.cn", user="ecshop", password="ecshop", database="ecshop",
                            charset='utf8', port=3306)
        sql = "select * from ecs_order_info where user_id=11402 and pay_status=2"
        order_id_db = database.readall(sql=sql)
        print(order_id_db)
        db_orderid = get_keywords(order_id_db, "order_id")
        print(db_orderid)
        """断言"""
        if pay_order_id in db_orderid:
            self.assertTrue(True)
        else:
            self.assertTrue(False)
if __name__ == '__main__':
    unittest.main()




