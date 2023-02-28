from django.views import View
from django.shortcuts import render, redirect
from .models import Tests


class TestCreateMixin(View):
    model = None
    def get(self, request):
        return render(request, 'tests/test_create.html')

    def post(self, request):
        data = []
        test_name = request.POST.get('test_name')
        for q in range(int(request.POST.get('questions-count'))):
            questions = dict()
            questions[f'question-{q}'] = request.POST.get(f'question-{q}')
            answers_mas = []
            for a in range(4):
                answers = dict()
                answers[f'answer[{a}][{q}]'] = request.POST.get(f'answer[{a}][{q}]')
                answers['answer_id'] = f'[{a}][{q}]'
                answers[f'is_correct[{a}[{q}]'] = True if request.POST.get(f'is_correct[{a}][{q}]') is not None else False
                answers_mas.append(answers)
            questions['answers'] = answers_mas
            data.append(questions)

        self.model.objects.create(test_name=test_name,
                                  questions=data,
                                  questions_count=int(request.POST.get('questions-count')))

        return redirect('tests_list_url')


class TestSolutionMixin(View):
    test_model = None
    correct_answers_model = None
    def get(self, request):
        rows = self.test_model.objects.get(id=request.GET.get('id'))
        return render(request, 'tests/test_solution.html', {'rows': rows})

    def post(self, request):
        dictionary = dict()
        row = Tests.objects.get(id=request.GET.get('id'))

        for q in range(int(request.POST.get('questions_count'))):
            for a in range(4):
                if row.questions[q]['answers'][a][f'is_correct[{a}[{q}]']:
                    a_id = row.questions[q]['answers'][a]['answer_id']

                    if request.POST.get(f'user_answer-[{a}][{q}]') == a_id:
                        dictionary[f'correct_user_answer_question[{q}]'] = a_id
        self.correct_answers_model.objects.create(true_answer=dictionary, test_id=request.GET.get('id'))
        return redirect('tests_list_url')







