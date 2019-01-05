import itchat
import time

itchat.auto_login()

friends = itchat.get_friends()


@itchat.msg_register(itchat.content.NOTE)
def blacklist(msg):
    if msg.MsgType == 10000:
        print(msg['Content'])
        file = open('blacklist.txt', 'a', encoding="utf-8")
        file.write(msg['Content'] + msg['FromUserName'] + '\n')
        file.close()


print('请输入群发内容')
blessing = input()
print('请输入群发间隔时间，建议3秒以上，单位：秒')
time_jg = input()
kssj = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
kssj_t = time.time()

for friend in friends:
    results = itchat.send(blessing, toUserName=friend['UserName'])
    if results['BaseResponse']['ErrMsg'] == '请求成功':
        print('已成功发送祝福给', friend['NickName'])
    time.sleep(time_jg)

jssj = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
jssj_t = time.time()
print('开始群发时间为：' + kssj)
print('结束群发时间为：' + jssj)
print('群发所用时间为：' + str((kssj_t - jssj_t) / 1000) + '秒')
itchat.run()
