from django import template
from puzzles.models import Puzzle, MetaPuzzle
from puzzles.forms import StatusForm

register = template.Library()

@register.inclusion_tag('puzzles_table.html')
def get_table(puzzles, request):
    answers = []
    table_class = []
    badge = []

    for (i, p) in enumerate(puzzles):
        answers.append(p.answer if p.answer else "")

        if p.status == Puzzle.PENDING:
            table_class.append("table-warning")
        elif p.status == Puzzle.SOLVED:
            table_class.append("table-success")
        elif p.status == Puzzle.STUCK:
            table_class.append("table-danger")
        else:
            table_class.append("")


        if MetaPuzzle.objects.filter(pk=p.pk).exists():
            badge.append("META")
        else:
            badge.append("")


    status_forms = [StatusForm(initial={'status': p.status}) for p in puzzles]
    return {'rows': zip(puzzles, answers, table_class, badge, status_forms)}


