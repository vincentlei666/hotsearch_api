
import xadmin
from xadmin import views





class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "九千热搜"  # 设置站点标题
    site_footer = "上海新新人类科技有限公司"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)

