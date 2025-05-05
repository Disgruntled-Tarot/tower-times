from django.db import models
import markdown

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField(help_text="Use Markdown formatting.")
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def get_markdown(self):
        import markdown
        return markdown.markdown(self.content)

class NarrativePrediction(models.Model):
    NARRATIVE_CHOICES = [
        ('displayed', 'Displayed Narrative'),
        ('hidden', 'Hidden Thread'),
    ]
    
    narrative_type = models.CharField(max_length=20, choices=NARRATIVE_CHOICES)
    prediction = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('fulfilled', 'Fulfilled'), ('failed', 'Failed')], default='pending')
    added_on = models.DateTimeField(auto_now_add=True)
    outcome_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"[{self.get_narrative_type_display()}] {self.prediction[:60]}"
