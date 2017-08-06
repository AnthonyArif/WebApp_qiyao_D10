import orm_module
from models import User, Blog, Comment
import asyncio


async def test_WEB04(loop):
    await orm_module.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')

    u = User(name='qiyao', email='qiyaofeng@123.com', passwd='123456', image='about:blank')

    await u.save()

'''
for x in test_WEB04():
    pass
'''

loop = asyncio.get_event_loop()
loop.run_until_complete(test_WEB04(loop))
loop.close()