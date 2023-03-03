from django.shortcuts import render, redirect
from .models import Tests, TrueAnswers
from django.views import View
from .services import *


def tests_list_view(request):
    rows = Tests.objects.all()
    dictionary = dict()
    for i in range(len(rows)):
        if TrueAnswers.objects.filter(test_id=rows[i].id).count():
            dictionary[i] = True
        else:
            dictionary[i] = False
    return render(request, 'tests/tests_list.html', context={'rows': rows, 'dictionary': dictionary})


class TestCreate(View):
    def get(self, request):
        return render(request, 'tests/test_create.html')

    def post(self, request):
        Tests.objects.create(test_name=create_test(request)[0],
                             questions=create_test(request)[1],
                             questions_count=int(request.POST.get('questions-count')))

        return redirect('tests_list_url')


class TestSolution(View):
    def get(self, request):
        return render(request, 'tests/test_solution.html', get_rows(request))

    def post(self, request):
        TrueAnswers.objects.create(true_answer=test_solution(request), test_id=request.GET.get('id'))
        return redirect('tests_list_url')


def check_test(request):

    return render(request, 'tests/check_test.html', get_ctx_for_check_test(request))
