from django.shortcuts import render, redirect, get_object_or_404
from .forms import GetRoute
from .models import Route, Question, Choice
from .functions import route_search, w_updater

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
    object_detail = get_object_or_404(Route, pk = page_id) # 특정 입력값의 결과 갖고 오는 코드
    
    # 아래 과정은 사용자가 입력한 선호 경로의 선택 횟수를 기록하기 위해 db를 업데이트하는 코드이다.
    straight_stair = Choice.objects.get(id=4)
    whirlpool_stair = Choice.objects.get(id=3)
    emergency_stair	= Choice.objects.get(id=2)
    elevator = Choice.objects.get(id=1)
    routes = [straight_stair, whirlpool_stair, emergency_stair, elevator]
    for choice in routes:
        if object_detail.route == choice.choice_text:
            choice.votes += 1
            choice.save()
            
            
    # 아래 코드는 그동안 사용자가 입력한 선호하는 입력수단을 기준으로 가장 선호하는 경로를 보여주기 위한 코드이다.
    # 한편, 전체 3개 층을 이동하는 과정에서 2개의 층을 올라가는 경우와 나머지 경우 소비자의 선호도가 극명하게 다르다.
    # 따라서 2개 층을 올라가는 경우와 나머지 경우 각각 가중치를 따로 계산한다.
    # 이를 위해 먼저 층 이동의 경루를 구분해 변수에 저장한다.
    total_response = []
    climb_two_floors = []
    others = []
    for object_test in Route.objects.all():
        total_response.append(object_test)
        
    
    for object in total_response:
        if int(object.start_point[1]) - int(object.end_point[1]) == -2:
            climb_two_floors.append(object)
        else:
            others.append(object)
    
    if int(object_detail.start_point[1]) - int(object_detail.end_point[1]) == -2: # 두 개의 층을 오르는 경우
        w = w_updater(climb_two_floors)
        recommended_path = route_search(object_detail.start_point, object_detail.end_point, w) 
    else: # 나머지 경우
        w = w_updater(others)
        recommended_path = route_search(object_detail.start_point, object_detail.end_point, w) 
        
        
        
    # 가장 짧은 경로를 찾는 경우, 특정 이동수단에 별도의 가중치를 부여하지 않는다.
    shortest_route = route_search(object_detail.start_point, object_detail.end_point, [0, 0, 0, 0])
    
    
    # 무조건 엘리베이터만을 이용하는 경로를 희망하는 경우, 다른 이동수단의 간선비용을 극단적으로 올려 엘리베이터 이용 결과만 나오도록 한다.
    elevator_route = route_search(object_detail.start_point, object_detail.end_point, [0, 1000, 1000, 1000])

    context ={}
    context['object_detail'] = object_detail
    context['shortest_route'] = shortest_route
    context['recommended_path'] = recommended_path
    context['elevator_route'] = elevator_route
    return render(request, 'navigation/result_page.html', context = context)
