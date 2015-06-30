from django.contrib import admin
from servicingly.models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.

class CategoryResource(resources.ModelResource):
	class Meta:
		model = Category

class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    pass


admin.site.register(ACL)
admin.site.register(Brand)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(Role)
admin.site.register(RoleMapping)
admin.site.register(ServiceCenter)
admin.site.register(TicketCategory)