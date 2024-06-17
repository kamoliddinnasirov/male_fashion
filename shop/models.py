from django.db import models, IntegrityError
from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from shop.abstract import BaseModel

UserModel = get_user_model()


class Category(BaseModel):
    name = models.CharField(max_length=60, verbose_name=_("name"))


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "Product category"
        verbose_name = "Category"
        verbose_name_plural = "2. Categories"


class ProductTag(BaseModel):
    name = models.CharField(max_length=60, verbose_name=_("name"))


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "Product tag"
        verbose_name = "Tag"
        verbose_name_plural = "6. Tags"


class BrandModel(BaseModel):
    name = models.CharField(max_length=60, verbose_name=_("name"))

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "Product brand"
        verbose_name = "Brand"
        verbose_name_plural = "3. Brands"


class SizeModel(BaseModel):
    name = models.CharField(max_length=60, verbose_name=_("name"))

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "Product size"
        verbose_name = "Size"
        verbose_name_plural = "4. Sizes"


class ColorModel(BaseModel):
    code = models.CharField(max_length=60, verbose_name=_("name"))

    def __str__(self) -> str:
        return self.code 
    
    class Meta:
        db_table = "Product color"
        verbose_name = "Color"
        verbose_name_plural = "5. Colors"


class ProductModel(BaseModel):
    title = models.CharField(max_length=60, verbose_name=_("title"))
    short_description = models.CharField(max_length=255, verbose_name=_("short description"))
    long_description = models.TextField(verbose_name=_("long description"))
    price = models.FloatField(verbose_name=_("price"))
    real_price = models.FloatField(verbose_name=_("real price"), default=0)
    sale = models.BooleanField(verbose_name=_("sale"), default=False)
    discount = models.PositiveSmallIntegerField(default=0, verbose_name=_("discount"))
    main_image = models.ImageField(upload_to="media/shop_product/%Y/%m/%d", verbose_name=_("main image"))
    category = models.ForeignKey(
        Category,
        on_delete=models.RESTRICT,
        related_name="products",
        verbose_name=_("category")
    )
    tags = models.ManyToManyField(
        ProductTag,
        related_name="products",
        verbose_name=_("tags")
    )
    sizes = models.ManyToManyField(
        SizeModel,
        related_name="products",
        verbose_name=_("sizes")
    )
    colors = models.ManyToManyField(
        ColorModel,
        related_name="products",
        verbose_name=_("colors")
    )
    brand = models.ForeignKey(
        BrandModel,
        on_delete=models.RESTRICT,
        related_name="products",
        verbose_name=_("brand"),
        null=True
    )

    class Meta:
        db_table = "Shop product"
        verbose_name = "Product"
        verbose_name_plural = "1. Products"


    def is_discount(self):
        return bool(self.discount)
    
    def new(self):
        return (timezone.now() - self.created_at).days <= 7
    
    @staticmethod
    def get_cart_info(self):
        cart = request.session.get("cart", [])#[67.4]
        if not cart:
            return 0, 0.0
        return len(cart), ProductModel.objects.filter(id__in=cart).aggregate(Sum("real_price"))['real_price__sum']
    
    @staticmethod
    def get_cart_objects(self):
        cart = request.session.get("cart", [])
        if not cart:
            return None
        return ProductModel.objects.filter(id__in=cart)

    

class Wishlist(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="wishlists", verbose_name=_("user"))
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name=_("product"))    


    @staticmethod
    def created_or_delete(user, product):
        try:
            return Wishlist.objects.create(user=user, product=product)
        except IntegrityError:
            return Wishlist.objects.get(user=user, product=product)
        
    def __str__(self) -> str:
        return f"{self.user.get_full_name()} | {self.product.title}"
    

    class Meta:
        db_table = "Wishlist"
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"
        unique_together = "user", "product",