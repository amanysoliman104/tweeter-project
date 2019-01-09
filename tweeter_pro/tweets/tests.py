# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy ,reverse
from .models import Tweet


User = get_user_model()
class TweetModelTestCase(TestCase):
    def setUp(self):
        some_random_user=User.objects.create(username='jitche33333333')



    def test_tweet_item(self):
        obj=Tweet.objects.create(
            user=User.objects.first(),
            content='some random content'
            )
        self.assertTrue(obj.content=="some random content")
        self.assertTrue(obj.id==1)
        absolute_url=reverse("tweet:detail",kwargs={"pk":1})
        self.assertEqual(obj.get_absolute_url() ,absolute_url)

    
    def test_tweet_url(self):
        obj=Tweet.objects.create(
            user=User.objects.first(),
            content='some random content'
            )
        absolute_url=reverse("tweet:detail",kwargs={"pk":obj.pk})
        self.assertEqual(obj.get_absolute_url() ,absolute_url)
