from django import forms
from forum.models import Question
from users.models import User


# class QuestionCreateForm(forms.Form):
#     user = forms.IntegerField()

#     title = forms.CharField(max_length=120)
#     text = forms.TextField()
#     views = forms.IntegerField()
    
    # def is_valid(self) -> bool:
    #     User.objects.filter(id=self.fields['user']).exists()
    #     return super().is_valid()


class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        # fields = [
        #     'user'
        # ]
