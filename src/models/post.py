__author__ = 'lhe'

import uuid
from src.common.database import Database
import datetime

__author__ = 'lhe'

class Post(object):

    def __init__(self, blog_id, title, content, author,
                 created_date = datetime.datetime.utcnow(),  # default 当前时间
                 _id = None): # default赋值后， 创建对象时可不引入该参数
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_data = created_date
        # generate random id if none, or else use user-specific
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert(collection ='posts',
                        query= self.json())

    # create the json form
    def json(self):
        return {
            '_id': self._id,
            'blog_id': self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_date': self.created_data
        }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'_id': id})
        return cls(**post_data)

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find('posts', {'blog_id': id})]



