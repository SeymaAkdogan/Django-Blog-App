from django.shortcuts import redirect, render
import json
from nutrition_record.models import Nutrition_Record
from posts.models import Category


def show(request):
    if request.user.is_authenticated:
        records = Nutrition_Record.objects.filter(user_id = request.user.id)
        repast_items_first={}
        repast_items_second={}
        repast_items_third={}
        for i in records:
            y = json.loads(i.repast)
            for c in y.keys():
                if i.day == 1:
                    repast_items_first[c]= y[c]
                elif i.day == 2:
                    repast_items_second[c] = y[c]
                elif i.day == 3:
                    repast_items_third[c] = y[c]

        return render(request,'nutrition_record/show_nutrition_record.html',{
            'categories' : Category.objects.all(),
            'record' : records,
            'repast_items_first' : repast_items_first,
            'repast_items_second' : repast_items_second,
            'repast_items_third' : repast_items_third,
        })
    else:
        return redirect('login')

def createNutritionRecord(request):
    if request.method == 'POST':
        day = request.POST['day']
        repast = request.POST['repast']
        meals = request.POST['meals']
        if request.user.is_authenticated:
            user = request.user
            first_record = Nutrition_Record.objects.filter(user_id=user.id,day=int(day))
            if first_record:
                user_record = Nutrition_Record.objects.get(user_id=user.id,day=int(day))
                if repast in json.loads(user_record.repast):
                    return render(request,'nutrition_record/create_nutrition_record.html',{
                        'error' : 'you already save this day',
                        'repast' : repast,
                        'meal' : meals,
                        'categories' : Category.objects.all()
                    }) 
                else:
                    db_repast_list = json.loads(user_record.repast)
                    db_repast_list[repast] = meals
                    user_record.repast = json.dumps(db_repast_list)
                    user_record.save()
                    return show(request)
            else:
                dict = {
                    repast: meals,
                }
                repast_list = json.dumps(dict)
                Nutrition_Record.objects.create(user_id=user,day=day,repast=repast_list)
                return show(request)
        else:
            return redirect('login')
    
    return render(request,'nutrition_record/create_nutrition_record.html',{
        'categories' : Category.objects.all()
    })
