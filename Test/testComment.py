import unittest 
from app.models import Comment,Post
from datetime import datetime

class test_commentModel(unittest.TestCase):

    # to test behaivours in the comment model

    def setUp(self):
        self.user_Me = User( firstname = 'Herrm' ,secondname = 'Mere',username = 'Memn', password = 'Hermer', email = 'hermemer@gmail.com')
        self.new_post = Post(title = 'test', content = 'testing is important',user_id =  1, category = 'interview',author='Me')
        self.new_comment =  Comment(name='name', email= 'e344536@gmail.com',content="content", post_id = 1)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.name, 'name')
        self.assertEquals(self.new_comment.email, 'e344536@gmail.com' )
        self.assertEquals(self.new_comment.content, 'content')
        self.assertEquals(self.new_comment.post_id, 1)
       

    def tearDown(self):
        Comment.query.delete()
        Post.query.delete()
    
    def test_save_Comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()),1)

    def test_delete_Comment(self):
        self.new_comment.delete_comment()
        self.assertTrue(len(Comment.query.all()),0)


    




