#encoding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Document(models.Model):
    class Meta:
        verbose_name = '擇優設計應交文件'
        verbose_name_plural = '擇優設計應交文件'
    
    stage_choice = (
            ('1', '準備階段'),
            ('2', '構想設計'),
            ('3', '初步設計'),
            ('4', '合約設計'),
            ('5', '細部設計'),
            )
    design_stage = models.CharField(max_length=32, choices=stage_choice, verbose_name='設計階段')
    document_sn = models.CharField(max_length=18, verbose_name='文件編號', blank=True)
    document_version = models.CharField(max_length=4, verbose_name='版次', blank=True)
    document_name = models.CharField(max_length=80, verbose_name='應交文件名稱')
    document_purpose = models.CharField(max_length=80, verbose_name='工作目的', blank=True)
    document_content = models.TextField(verbose_name='工作內容', blank=True)

    risk = models.TextField(verbose_name='風險評估及討論', blank=True)
    design_follows = models.TextField(verbose_name='設計依據／法規', blank=True)
    document_ref = models.TextField(verbose_name='參考文件', blank=True)

    author = models.CharField(max_length=64, verbose_name='承辦人')
    def __unicode__(self):
        return self.document_name
