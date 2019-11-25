from django.forms import ModelForm
from blogging.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'published_date']

"""
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
"""
