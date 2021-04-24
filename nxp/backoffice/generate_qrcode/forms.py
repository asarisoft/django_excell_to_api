# from SahabatElvineDjango.apps.news.models import News
# from django import forms


# class AddNewsForm(forms.ModelForm):
#     name = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control'}), required=False)
#     description = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
#     short_description = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
#     picture1 = forms.ImageField(
#         required=True, help_text="Ukuran gambar harus 500PX * 270PX")
#     picture2 = forms.ImageField(required=False)
#     picture3 = forms.ImageField(required=False)
#     date = forms.ImageField(required=False)

#     class Meta:
#         model = News
#         fields = '__all__'

#     def clean_picture1(self):
#         picture1 = self.cleaned_data.get('picture1', False)
#         if picture1:
#             if picture1.size > 0.5 * 1024 * 1024:
#                 raise forms.ValidationError(
#                     "picture1 file too large ( > 0.5mb )")
#         return picture1

#     def clean_picture2(self):
#         picture2 = self.cleaned_data.get('picture2', False)
#         if picture2:
#             if picture2.size > 0.5 * 1024 * 1024:
#                 raise forms.ValidationError(
#                     "picture2 file too large ( > 0.5mb )")
#         return picture2

#     def clean_picture3(self):
#         picture3 = self.cleaned_data.get('picture3', False)
#         if picture3:
#             if picture3.size > 0.5 * 1024 * 1024:
#                 raise forms.ValidationError(
#                     "picture3 file too large ( > 0.5mb )")
#         return picture3
