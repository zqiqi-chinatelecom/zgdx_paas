# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1535722677.367
_enable_loop = True
_template_filename = 'E:/STUDY/cloud/tempt/zgdx_paas/framework/framework/templates/home_application/helloworld.html'
_template_uri = '/home_application/helloworld.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'hello world from zqiqi')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "27": 21, "21": 1}, "uri": "/home_application/helloworld.html", "filename": "E:/STUDY/cloud/tempt/zgdx_paas/framework/framework/templates/home_application/helloworld.html"}
__M_END_METADATA
"""
