import requests
import json


class SendMethod:
    @staticmethod
    def send_post(url=None,data=None):
        request_data={"json":json.dumps(data)}
        response=requests.post(url=url,data=request_data)
        return response.json()  # 接口返回值为json格式

if __name__ == '__main__':
    url="http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
    data={"name":"cooper","password":"123456"}
    SendMethod.send_post(url=url,data=data)




