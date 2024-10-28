from django import forms
from django.contrib.auth import get_user_model
from .models import Team

User = get_user_model()

class TeamAndUserCreationForm(forms.ModelForm):
    # ユーザー情報
    username = forms.CharField(label="ユーザー名", max_length=100) 
    email = forms.EmailField(label="メールアドレス", max_length=100) 
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput)
    
    class Meta:
        model = Team
        fields = ['team_name']  # チームのフィールドのみ設定
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("このメールアドレスはすでに登録されています。別のメールアドレスを使用してください。")
        return email

    def save(self, commit=True):
        # チームをまず保存
        team = super().save(commit=commit)
        
        # ユーザーを作成し、チームと関連付け
        user = User(
            email=self.cleaned_data['email'],  # メールアドレスを使用
            username=self.cleaned_data['username'],  # ユーザー名を使用
            team=team  # 作成したチームと紐付け
        )
        user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()
        
        return team, user  # チームとユーザーを返す