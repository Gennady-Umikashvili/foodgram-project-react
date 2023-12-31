from django.contrib import admin
from django import forms

from .models import (
    Ingredient,
    Recipe,
    Amount,
    Tag,
    Favorite,
    UserCart,
    User,
    Follow
)

admin.site.register(Favorite)
admin.site.register(UserCart)
admin.site.register(Follow)
admin.site.register(Tag)


class InlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        super().clean()
        if len([form for form in self.forms if
                form.cleaned_data.get('DELETE')]) == len(self.forms):
            raise forms.ValidationError("Нельзя удалить все ингредиенты")


class IngredientInline(admin.TabularInline):
    model = Recipe.ingredients.through
    min_num = 1
    formset = InlineFormset
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "count_favorites")
    list_filter = ("author", "name", "tags")
    inlines = (IngredientInline,)

    def count_favorites(self, recipe):
        return recipe.favorite_by_user.count()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("username", "email")


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'measurement_unit')
    list_filter = ('name',)


@admin.register(Amount)
class AmountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'recipe', 'ingredient', 'amount')
    list_editable = ('ingredient', 'amount')
