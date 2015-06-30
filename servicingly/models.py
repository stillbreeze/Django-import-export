from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class ACL(models.Model):
    AclTitle = models.CharField(_("ACL title"), max_length=255)

    def __str__(self):
        return self.AclTitle


class Brand(models.Model):
    brandTitle = models.CharField(_("Brand title"), max_length=255)

    def __str__(self):
        return self.brandTitle


class Category(models.Model):
    categoryTitle = models.CharField(_("Category title"), max_length=255)
    brand = models.ForeignKey(Brand)

    def __str__(self):
        return self.categoryTitle


class Product(models.Model):
    productTitle = models.CharField(_("Product title"), max_length=255)
    brand = models.ForeignKey(Brand)

    def __str__(self):
        return self.productTitle


class ProductDetail(models.Model):
    productDetailTitle = models.CharField(_("Product detail title"), max_length=255)
    product = models.ForeignKey(Product)

    def __str__(self):
        return self.productDetailTitle


class Role(models.Model):
    roleTitle = models.CharField(_("Role title"), max_length=255)

    def __str__(self):
        return self.roleTitle


class RoleMapping(models.Model):
    roleMappingTitle = models.CharField(_("Role mapping title"), max_length=255)

    def __str__(self):
        return self.roleMappingTitle


class ServiceCenter(models.Model):
    serviceCenterTitle = models.CharField(_("Service center title"), max_length=255)

    def __str__(self):
        return self.serviceCenterTitle


class TicketCategory(models.Model):
    ticketCategoryTitle = models.CharField(_("Ticket category title"), max_length=255)

    def __str__(self):
        return self.ticketCategoryTitle
