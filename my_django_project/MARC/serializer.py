from rest_framework import serializers
from .models import ProductInfo, ProductionProductInfo, ProductFeedback


class ProductInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductInfo
        fields = ('sl_no', 'id', 'name_of_product', 'type_of_product',
                  'firmware_version', 'os_supported', 'supported_protocols',
                  'max_firmware_support', 'env_support', 'power_capability',
                  'pricing', 'configurable', 'desc')


class ProductionProductInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductionProductInfo
        fields = ('sl_no', 'name_of_product', 'type_of_product',
                  'firmware_version', 'username', 'customer_id',
                  'last_Upgraded', 'validity', 'alarms','health',
                  'auto_recovery', 'last_rebooted', 'system_crash_report',
                  'security', 'authority')


class ProductFeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductFeedback
        fields = ('username', 'product_name', 'product_type',
                  'services', 'product_quality', 'suggestions',
                  'future_scope')