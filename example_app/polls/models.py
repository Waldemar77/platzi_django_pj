from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):

    # Attributes of this class are the columns of the a table
    # Id column it isn't necessary wrote because Django sets it automatically
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text
    
    def was_recent_question(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    
    # For foreign key, we need to specify the class wherein the primary key is.
    # "on_delete=models.CASCADE" is used to delete another answers that doesn't match with key.
    question =models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
