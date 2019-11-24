from django.db import models

class Puzzle(models.Model):
    name = models.CharField(max_length=128)
    hunt = models.ForeignKey('hunts.Hunt', on_delete=models.CASCADE, related_name='puzzles')
    url = models.URLField()

    sheet = models.URLField()
    channel = models.URLField()
    notes = models.TextField(default="")

    SOLVING = ''
    PENDING = 'PENDING'
    SOLVED = 'SOLVED'
    STUCK = 'STUCK'
    STATUS_CHOICES = [SOLVING, PENDING, SOLVED, STUCK]

    status = models.CharField(
        max_length=10,
        choices=[(status, status) for status in STATUS_CHOICES],
        default=SOLVING)
    answer = None

class MetaPuzzle(Puzzle):
    feeder = models.ManyToManyField('Puzzle', related_name='feeders')
