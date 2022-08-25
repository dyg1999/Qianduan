from django.urls import path
from blog import api,payapi

urlpatterns = [
    path('article-like/',api.articleLike),
    path('article-favor/',api.articleFavor),
    # 文章查看
    path('article-data/',api.articleData),
    
    # 文章发布
    path('add-article/',api.add_article),
    # 文章列表
    path('article-list/',api.articleList),
    # 文章删除
    path('delete-article/',api.deleteArticle),
    path('user-article-info/',api.userArticleInfo),
    
    # 用户管理
    # 登录
    path('dygweb-login/',api.dygweb_login),
    # 注册
    path('dygweb-register/',api.dygweb_register),
    # 自动登录
    path('auto-login/',api.dygweb_autoLogin),
    # 登出
    path('dygweb-logout/',api.dygweb_logout),
    # 鉴权
    path('dygweb-checkperm/',api.dygweb_checkPerm),
    # 用户组
    path('dygweb-group/',api.dygweb_group),
    # 用户列表
    path('dygweb-userlist/',api.dygweb_userlist),
    # lanmu_tree
    path('dygweb-lanmu/',api.dygweb_lanmu),
    # 评论
    path('pinglun/',api.dygweb_pinglun),

    # 打赏
    path('get-alipay-url/',payapi.getAlipayUrl),
    
    

    
    

]