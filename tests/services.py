from .models import Tests, TrueAnswers
from django.shortcuts import redirect


def create_test(request):
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
    return test_name, data


def test_solution(request):
    dictionary = dict()
    row = Tests.objects.get(id=request.GET.get('id'))

    for q in range(int(request.POST.get('questions_count'))):
        for a in range(4):
            if row.questions[q]['answers'][a][f'is_correct[{a}[{q}]']:
                a_id = row.questions[q]['answers'][a]['answer_id']

                if request.POST.get(f'user_answer-[{a}][{q}]') == a_id:
                    dictionary[f'correct_user_answer_question[{q}]'] = a_id
    return dictionary


def get_rows(request):
    ctx = {
        'rows': Tests.objects.get(id=request.GET.get('id'))
    }
    return ctx


def get_ctx_for_check_test(request):
    test = Tests.objects.get(id=request.GET.get('id'))
    answ = TrueAnswers.objects.filter(test_id=request.GET.get('id'))
    x = len(answ) - 1
    ctx = {
        'test': test.test_name,
        'answers': f'{len(answ[x].true_answer)}/ {test.questions_count}'
    }
    return ctx
