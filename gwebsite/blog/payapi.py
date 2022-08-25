from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from blog.models import Article,PayOrder
import datetime
import random


# 客户端配置
from alipay.aop.api.AlipayClientConfig import AlipayClientConfig 
# 默认客户端
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
# 网站支付数据模型类
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.domain.SettleInfo import SettleInfo
# 网站支付请求类
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest
from alipay.aop.api.util.SignatureUtils import verify_with_rsa


@api_view(['POST'])
def getAlipayUrl(request):
    token = request.POST['token']
    user_token = Token.objects.filter(key=token)
    if len(user_token) == 0:
        return Response('nologin')
    
    user = user_token[0].user
    article_id = request.POST['article_id']
    article = Article.objects.get(id=article_id)
    new_payorder = PayOrder(belong_user=user,belong=article)
    nowtime = datetime.datetime.now()
    new_payorder.order = str(nowtime.year) + str(random.randrange(10000000,99999999))
    print(new_payorder.order)
    new_payorder.price = '9.9'
    
    alipay_client_config = AlipayClientConfig()
    alipay_client_config.server_url = 'https://openapi.alipay.com/gateway.do'
    alipay_client_config.app_id = '[your app_id]'
    alipay_client_config.app_private_key = '[your app private key]'
    alipay_client_config.alipay_public_key = '[alipay public key]'
    
    
    
    pay_link = ""
    return Response({'pay_link':pay_link})