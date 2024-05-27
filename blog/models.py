from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.abstract import BaseModel


class Author(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=_("full name"))
    image = models.ImageField(upload_to="author_image/", verbose_name=_("image"))


    class Meta:
        verbose_name=_("Author")
        verbose_name_plural = _("Authors")


    def __str__(self) -> str:
        return self.full_name
    

class PostTag(BaseModel):
    name = models.CharField(max_length=30, verbose_name=_("name"))

    class Meta:
        verbose_name=_("Tag")
        verbose_name_plural=_("Tags")


    def __str__(self) -> str:
        return self.name
    

class Post(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    body = models.TextField(verbose_name=_("body"))
    main_image=models.ImageField(upload_to="post_image/", verbose_name=_("main image"))
    author = models.ForeignKey(Author, related_name="posts", on_delete=models.RESTRICT)
    tag = models.ManyToManyField(PostTag, related_name="posts", verbose_name=_("tag"))



    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self) -> str:
        return f"{self.title[:100]} ..." 
    

class Comment(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    email = models.EmailField(verbose_name=_("email"))
    phone = models.CharField(max_length=13, verbose_name=_("phone"))
    comment = models.TextField(verbose_name=_("comment"))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", verbose_name=_("post"))


    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")


    def __str__(self) -> str:
        return f"{self.name}\n{self.email}\n{self.phone}\n{self.comment[:50]}..."
    
    