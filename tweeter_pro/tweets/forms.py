from django import forms
from .models import Tweet

class TweetModelForm(forms.ModelForm):
	content=forms.CharField(label='',
	    widget=forms.Textarea(attrs={'placeholder':" your mesage","class":"form-control"})) #to make taxt label for tweet
	class Meta:
		model =Tweet
		fields=[
			
			#"user",
			"content"
		]
		#exclude= ['user']
	

	'''def clean_content(self,*args,**kwargs):
		content=self.cleaned_data.get("content")
		if content=="abc":
			raise forms.ValidationError("cannot be abc")
		return content
		pass'''

	