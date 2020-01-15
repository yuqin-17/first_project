"""
对pymysql进行二次封装 , 方便之后调用
"""
# 导入pymysql
import pymysql


class Database(object):
    def __init__(self,host="localhost",user="root",password=None,database=None,charset='utf8',port=3306):
        # 创建连接对象
        self.cnn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=port
        )

    def readall(self, sql, args=None):
        """
        读取所有数据
        :param sql: 需要执行的sql语句
        :param args: sql语句需要的参数
        :return:
        """
        # 创建游标对象
        with self.cnn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            # 使用游标对象执行sql
            cursor.execute(sql,args)
            # 获取结果
            data = cursor.fetchall()
        # 关闭游标(不用关闭)

        # 返回数据
        return data

    def readone(self, sql, args=None):
        """
        读取一条数据
        :param sql: 需要执行的sql语句
        :param args: sql语句需要的参数
        :return:
        """
        # 创建游标对象
        with self.cnn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            # 使用游标对象执行sql
            cursor.execute(sql, args)
            # 获取结果
            data = cursor.fetchone()
        # 关闭游标(不用关闭)

        # 返回数据
        return data

    def write(self,sql,args=None):
        """
        写入数据
        :param sql:  sql语句
        :param args:  sql的参数
        :return:
        """
        try:
            #创建游标对象
            with self.cnn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
                #开启事务
                #执行sql
                rows = cursor.execute(sql,args)
                if rows == 0:
                    # 说明执行失败
                    raise Exception("操作失败,受影响的行数为0")
                # 提交事务
                self.cnn.commit()
                # 返回true
                return True
        except Exception as e:
            # 捕获异常说明执行失败,回滚
            self.cnn.rollback()
            print("执行失败!",e)
            return False


    def __del__(self):
        # 对象被销毁自动执行
        # 关闭连接
        self.cnn.close()


