#encoding=utf-8
from __future__ import unicode_literals

from django.db import models

from decimal import Decimal

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=255,verbose_name="公司名稱")
    company_address = models.CharField(max_length=255,verbose_name="公司地址")
    product = models.TextField(verbose_name="主力產品")
    main_customer = models.TextField(verbose_name="主要客戶",blank=True)
    capital = models.DecimalField(max_digits=16, decimal_places=0, verbose_name="資本額", default=Decimal(0))
    current_tech = models.TextField(max_length=1024,verbose_name="目前技術及設計能量")
    tools = models.CharField(max_length=1024,verbose_name="生產及測試設備")
    export_pemission = models.CharField(max_length=1024,verbose_name="輸出許可")
    authentication = models.CharField(max_length=1024,verbose_name="證書",blank=True)
    collab_willing = models.NullBooleanField(verbose_name="合作意願")
    discussion = models.TextField(verbose_name="討論事項",blank=True)
    comment = models.TextField(verbose_name="建議事項", blank=True)
    attachemnt = models.FileField(verbose_name="附件", blank=True)
    def __unicode__(self):
        return self.company_name
