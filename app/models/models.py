from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=10)

# 블로그 - Model
# 사용자(User)
#     name
#     # 중개테이블 쓰지 않고, 각각 MTM으로 지정
#     friends
#     block_users
#
# 사용자 정보(UserInfo)
#     # OTO으로 User와 연결
#     address
#     phone_number
#
# 글(Post)
#     user
#     title
#     content
#     created_at
# 글의 좋아요 (PostLike)
#     post
#     user
#     created_at
# 댓글(Comment)
#     user
#     content
#     created_at
# 댓글의 좋아요 (CommentLike)
#     comment
#     user
#     created_at
#
#
# 사용자 모델
# @프로퍼티
# comments:
#     자신이 작성한 모든 댓글 QuerySet리턴
#
# posts:
#     자신이 작성한 모든 글 QuerySet리턴
#
# 글 모델
# @프로퍼티
# like_users:
#     이 글에 좋아요를 누른 유저 QuerySet리턴
#
# 댓글 모델
# @프로퍼티
# like_users:
#     이 댓글에 좋아요를 누른 유저 QuerySet리턴