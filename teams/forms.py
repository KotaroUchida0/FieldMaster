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



class UserCreationForm(forms.ModelForm):
    POSITION_CHOICES = [
        ('P', 'ピッチャー'),
        ('C', 'キャッチャー'),
        ('IF', '内野手'),
        ('OF', '外野手'),
    ]

    BAT_THROW_CHOICES = [
        ('RR', '右投げ右打ち'),
        ('RL', '右投げ左打ち'),
        ('LR', '左投げ右打ち'),
        ('LL', '左投げ左打ち'),
    ]

    username = forms.CharField(label="ユーザー名", max_length=100)
    email = forms.EmailField(label="メールアドレス", max_length=100)
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput)
    bat_throw = forms.ChoiceField(label="投打", choices=BAT_THROW_CHOICES)
    jersey_number = forms.IntegerField(label="背番号", required=False)
    position = forms.ChoiceField(label="ポジション", choices=POSITION_CHOICES)
    role = forms.CharField(label="役割", max_length=50, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bat_throw', 'jersey_number', 'position', 'role']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("このメールアドレスはすでに登録されています。別のメールアドレスを使用してください。")
        return email

    def save(self, commit=True, team=None):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        # その他のフィールドを追加
        user.bat_throw = self.cleaned_data['bat_throw']
        user.jersey_number = self.cleaned_data.get('jersey_number')
        user.position = self.cleaned_data['position']
        user.role = self.cleaned_data.get('role')

        # チームをセット
        if team:
            user.team = team

        if commit:
            user.save()

        return user
