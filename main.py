from json import dumps
from requests import post
from os import environ


def main():
    # get pushplus token
    token = environ.get('token')

    if not token:
        # 无token则拦截推送
        return 'PushPlus: 未配置token，无法进行消息推送。'
    url = 'http://www.pushplus.plus/send/'
    headers = {'Content-Type':'application/json'}
	
	# api_list: [https://api.03c3.cn/zb, https://api.vvhan.com/api/60s, https://api.emoao.com/api/60s]
    data = {
        "token": token,
        "title": "每日新闻推送 bot",
        "content": "<img src='https://api.03c3.cn/zb' /><img src='https://api.emoao.com/api/60s' />",
        "template": "html",
        "channel": "wechat"
    }
    data = dumps(data).encode(encoding='utf-8')
    rsp = post(url=url, data=data, headers=headers)


if __name__ == '__main__':
    main()
