from django import forms
from django.contrib import admin

from .models import Item, OrderItem, Order, Payment, Coupon, BillingAddress, Category, Slide, Review

from ckeditor.widgets import CKEditorWidget


# Register your models here.

# Custom method to display detailed billing address
def detailed_billing_address(obj):
    if obj.billing_address:
        return f"{obj.billing_address.street_address}, {obj.billing_address.apartment_address}, {obj.billing_address.country}, {obj.billing_address.zip}"
    return "No billing address"

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    detailed_billing_address,
                    'being_delivered',
                    'received',
                    'payment',
                    'coupon',
                    ]
    list_display_links = [
        'user',
        'payment',
        'coupon'
    ]
    list_filter = ['user',
                   'ordered',
                   'being_delivered',
                   'received',]
    search_fields = [
        'user__username',
        'ref_code'
    ]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']


def copy_items(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()


copy_items.short_description = 'Copy Items'

class ItemAdminForm(forms.ModelForm):
    description_long = forms.CharField(widget=CKEditorWidget(config_name='default'))

    class Meta:
        model = Item
        fields = '__all__'

class ItemAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
    ]
    list_filter = ['title', 'category']
    search_fields = ['title', 'category']
    prepopulated_fields = {"slug": ("title",)}
    actions = [copy_items]
    form = ItemAdminForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_active'
    ]
    list_filter = ['title', 'is_active']
    search_fields = ['title', 'is_active']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Slide)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(BillingAddress, AddressAdmin)
admin.site.register(Review)
