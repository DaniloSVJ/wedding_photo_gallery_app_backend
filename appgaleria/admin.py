from django.contrib import admin
from django import forms
import pandas as pd
from .models import Photo, Comment, Like, UserProfile,UploadedExcel
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User
class UserProfileAdmin(DefaultUserAdmin):
    list_display = ('email', 'is_staff', 'user_type')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        (None, {
            'fields': ('email', 'username')
        }),
        ('Permissions and Status', {
            'fields': ('user_type', 'is_active', 'is_staff', 'password', 'first_name', 'last_name')
        }),
    )

admin.site.register(UserProfile, UserProfileAdmin)



@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['userUpload', 'timestamp', 'approved']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo', 'content', 'timestamp']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo']

class ExcelUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedExcel
        fields = ['file']

class UploadedExcelAdmin(admin.ModelAdmin):
    list_display = ['file', 'uploaded_at']
    form = ExcelUploadForm

    def save_model(self, request, obj, form, change):
        obj.save()
        # Processamento do arquivo após o salvamento
        process_excel_file(obj.file.path)

def process_excel_file(file_path):
    print("Processando arquivo:", file_path)  

    df = pd.read_excel(file_path)

    for index, row in df.iterrows():
        email = row['email']
        username = row['username']
        password = row.get('password')

        if not email or not username:
            continue  
        try:
            user = UserProfile.objects.create_user(username=username, email=email, password=password)
            print(f"Usuário {username} criado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar usuário na linha {index}: {e}")

admin.site.register(UploadedExcel, UploadedExcelAdmin)





