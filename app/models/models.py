from django.db import models

# on_delete 에 SET_NULL, CASCADE, SET_DEFALT 넣어봐서 뭐가 다른지 써볼 것
class User(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField(
        'self',
    )
    block_users = models.ManyToManyField(
        'self',
        symmetrical=False,
    )

    def __str__(self):
        return self.name

    @property
    def comments(self):
        return self.comment_set.all()

    @property
    def posts(self):
        return self.post_set.all()


class UserInfo(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )

    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user} 님의 주소는 {self.address} 연락처는 {self.phone_number}'


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.user},{self.title}\n {self.content}\n{self.created_at}'

    @property
    def total_like(self):
        return f'총 {len(self.postlike_set.all())} 개의 좋아요'

    @property
    def like_users(self):
        like_users = []
        for postlike in self.postlike_set.all():
            like_users.append(postlike.user)
        return like_users


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post,
        on_delete=models.SET_DEFAULT,
        default=True,
    )

    def __str__(self):
        return f'{self.user} 님이,{self.post.title} 글에 대해, {self.content}, {self.created_at}'


class PostLike(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} 님이, {self.post.title} 에 좋아요 클릭.'



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