# -*- coding:utf-8 -*-
# from rest_framework import settings

#'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',

from rest_framework.views import exception_handler

from rest_framework.views import exception_handler
# from luffyapi.utils import response
from .response import APIResponse
from .logging import logger
def common_exception_handler(exc, context):
    logger.error('view是：%s ，错误是%s'%(context['view'].__class__.__name__,str(exc)))
    print(context['view'].__class__.__name__)
    ret=exception_handler(exc, context)

    if not ret:
        if isinstance(exc,KeyError):
            return APIResponse(code=0, msg='key error')

        return APIResponse(code=0,msg='error',result=str(exc))
    else:
        return APIResponse(code=0,msg='error',result=ret.data)






