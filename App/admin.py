from django.contrib import admin
from .models import Portfolio
from .models import Nome

class adminPort(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

admin.site.register(Nome, adminPort)

class adminPro(admin.ModelAdmin):
    list_display = ('name', 'data', 'descricao', 'link', 'nome', 'python', 'java', 'css', 'html', 'javascript', 'c',  )
    search_fields = ('name', )

admin.site.register(Portfolio, adminPro)