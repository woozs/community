#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/10 14:35
# @Author  : mrwuzs
# @Site    :
# @File    : manager.py
# @Software: PyCharm
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, email, passwod, **kwargs):
        """
        create user
        :param username:
        :param email:
        :param passwod:
        :param kwargs:
        :return:
        """
        if not email:
            raise ValueError("User must have avalid email address .")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(
            passwod
        )
        user.save()

        return user

    def create_superuse(self, username, email, passwod, **kwargs):
        """
        create a super user
        :param username:
        :param email:
        :param passwod:
        :param kwargs:
        :return:
        """
        user = self.create_user(username, email, passwod, **kwargs)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
