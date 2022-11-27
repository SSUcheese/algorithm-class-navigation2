from django.shortcuts import render, redirect, get_object_or_404
from .forms import GetRoute
from .models import Route, Question, Choice
from .functions import route_search

# Create your views here.

def page_view(request):
    question_list = Question.objects.get(pk=1)
    context = {'question_list':question_list}
    return render(request, 'navigation/index.html', context=context)


def detail(request):
    if request.method == 'POST':
        form = GetRoute(request.POST)
        if form.is_valid():
            new_route = form.save()
            return redirect('route_result', page_id =new_route.id)
    else:
        form = GetRoute()
    return render(request, 'navigation/get_route.html', {'form':form})
    

def detail_route(request, page_id):
    object_detail = get_object_or_404(Route, pk = page_id)
    straight_stair = Choice.objects.get(id=4)
    whirlpool_stair = Choice.objects.get(id=3)
    emergency_stair	= Choice.objects.get(id=2)
    elevator = Choice.objects.get(id=1)
    # test = []
    # for object_test in Route.objects.all():
    #     test.append(object_test)
    routes = [straight_stair, whirlpool_stair, emergency_stair, elevator]
    for choice in routes:
        if object_detail.route == choice.choice_text:
            choice.votes += 1
            choice.save()
    result_route = route_search(object_detail.start_point, object_detail.end_point)
    context ={}
    context['object_detail'] = object_detail
    context['result_route'] = result_route
    # context['test'] = test
    return render(request, 'navigation/result_page.html', context = context)
