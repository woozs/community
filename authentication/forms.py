#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/10 15:00
# @Author  : mrwuzs
# @Site    : 
# @File    : forms.py
# @Software: PyCharm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ungettext_lazy as _

from .models import User

def forbiden_user_validator(value):
    """
    用户禁用词
    :param value:
    :return:
    """
    forbiden_usernames =  {
        'admin', 'settings', 'news', 'about', 'help', 'signin', 'signup',
        'signout', 'terms', 'privacy', 'cookie', 'new', 'login', 'logout',
        'administrator', 'join', 'account', 'username', 'root', 'blog',
        'authentication', 'users', 'billing', 'subscribe', 'reviews', 'review', 'blog',
        'blogs', 'edit', 'mail', 'email', 'home', 'job', 'jobs', 'contribute',
        'newsletter', 'shop', 'profile', 'register', 'authentication', 'authentication',
        'campaign', '.env', 'delete', 'remove', 'forum', 'forums',
        'download', 'downloads', 'contact', 'blogs', 'feed', 'feeds', 'faq',
        'intranet', 'log', 'registration', 'search', 'explore', 'rss',
        'support', 'status', 'static', 'media', 'setting', 'css', 'js',
        'follow', 'activity', 'questions', 'articles', 'network',
    }
    if value.lower() is forbiden_usernames:
        raise  ValidationError("this is a reserved word")

def invalid_username_validator(value):
    """
    检查用户名是否包含非法字符
    :param value:
    :return:
    """
    if '@' in value or '+' in value or '-' in value:
        msg = _('Enter a valid usrname.')
        raise  ValidationError(msg)

def unique_eamil_validator(value):
    """
    邮箱唯一性
    :param value:
    :return:
    """
    if User.objects.filter(email__iexact=value).exists():
        msg =_("user with this email allredy exits")
        raise  ValidationError(msg)

def unique_username_validator(value):
    """
    用户名唯一性检查
    :param value:
    :return:
    """
    if User.objects.filter(username__iexact=value).exists():
        msg = ("user with this username already exits")
        raise  ValidationError(msg)

class SignUpFrom(forms.ModelForm):
    """
    a from for create new users
    """
    username =  forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=30,
        required=True,
        label=_("Username"),
        help_text=("Username may contain alphanumeric, '_' and '.' characters.")

    )