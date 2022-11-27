from email.policy import default
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(verbose_name='질문내용', max_length=50)
    
    def __str__(self):
        return self.question_text


class Route(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ROUTE_CHOICES = [
        ('straight_stair', 'straight_stair'), # 앞에 값은 db에 저장되는 값, 뒤에 값은 실제 표시되는 값
        ('whirlpool_stair', 'whirlpool_stair'),
        ('emergency_stair', 'emergency_stair'),
        ('elevator', 'elevator')
    ]
    
    start_point = models.CharField(max_length=50)
    end_point = models.CharField(max_length=50)
    route = models.CharField(choices=ROUTE_CHOICES, max_length=50, default=True)
    point = [start_point, end_point]
    
    # def __str__(self):
    #     return self.point
    

class Choice(models.Model):
    # 각 이동경로 선택된 횟수 기록
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(verbose_name='선택지', max_length=50)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
    