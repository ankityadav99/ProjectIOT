from django.contrib import admin
from .models import ProductInfo, ProductionProductInfo, ProductFeedback


class AdminProductInfo(admin.ModelAdmin):
    list_display = ('sl_no', 'id', 'name_of_product', 'type_of_product',
              'firmware_version', 'os_supported', 'supported_protocols',
              'max_firmware_support', 'env_support', 'power_capability',
              'pricing', 'configurable', 'desc')

    """
    # This is used to enable editing
    
    list_editable = ('firmware_version', 'supported_protocols',
                     'max_firmware_support', 'env_support',
                     'pricing', 'configurable', 'desc')
    """


class AdminProductionProductInfo(admin.ModelAdmin):
    list_display = ('sl_no', 'name_of_product', 'type_of_product', 'firmware_version',
                    'username', 'customer_id', 'last_Upgraded', 'validity',
                    'alarms','health','auto_recovery','last_rebooted',
                    'system_crash_report','security','authority')


class AdminProductFeedback(admin.ModelAdmin):
    list_display = ('username', 'product_name', 'product_type',
                    'services', 'product_quality', 'suggestions',
                    'future_scope')


# Register your models here.
admin.site.register(ProductInfo, AdminProductInfo)
admin.site.register(ProductionProductInfo ,AdminProductionProductInfo)
admin.site.register(ProductFeedback, AdminProductFeedback)
