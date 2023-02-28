from django.shortcuts import render
from .models import Tests, TrueAnswers
from .utils import TestCreateMixin, TestSolutionMixin


def tests_list_view(request):
    rows = Tests.objects.all()
    return render(request, 'tests/tests_list.html', context={'rows': rows})


class TestCreate(TestCreateMixin):
    model = Tests


class TestSolution(TestSolutionMixin):
    test_model = Tests
    correct_answers_model = TrueAnswers


def check_test(request):
    test = Tests.objects.get(id=request.GET.get('id'))
    answ = TrueAnswers.objects.get(id=request.GET.get('id'))
    dictt = {'test': test.test_name, 'answers': f'{len(answ.true_answer)}/ {test.questions_count}'}
    return render(request, 'tests/check_test.html', context=dictt)

