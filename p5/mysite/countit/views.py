from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect

calories = 0 
name , age, weight , gender = '' , '' , '' , '' 
bv , ldv , dv , sv , drv = False , False , False , False , False

def home_view(request):
    return render(request,'countit/index.html')

def show_form(request):
    global name, age, gender, weight, calories,bv ,ldv,sv, drv
    if request.method == "GET":
        return  render(request, 'countit/form.html')
    if request.method == "POST":
        data = request.POST
        calories = 0
        name = data['name']
        age = data['age']
        weight = data['weight']
        gender = data['gender']
        #bv , ldv , sv , drv = False , False , False , False , False
        return  HttpResponseRedirect('/breakfast/')

def breakfast(requst):
    global calories,bv
    if requst.method == "GET":
        if bv:
            return HttpResponseRedirect('/')
        return render(requst, 'countit/breakfast.html')
    if requst.method == "POST":
        b1 = requst.POST["egg"]
        b2 = requst.POST["butter"]
        b4 = requst.POST["peanut butter"]
        b5 = requst.POST["honey"]
        b6 = requst.POST["jam"]
        b7 = requst.POST["halva shekari"]
        b8 = requst.POST["cornflex"]
        b9 = requst.POST["Breakfast chocolate"]
        b10 = requst.POST["Tomato omelette"]
        b11 = requst.POST["khameh"]
        b12 = requst.POST["Mushroom omelette"]
        b13 = requst.POST["adasi"]
        b14 = requst.POST["bread"]
        b15 = requst.POST["white cheese"]
        b16 = requst.POST["creamy cheese"]
        b17 = requst.POST["boiled egg"]
        b18 = requst.POST["Liquon cheese"]
        if( b1 !='' ):
            calories += int(b1)*78
        if ( b2 !='' ):
            calories += int(b2)*45
        if ( b4 !='' ):
            calories += int(b4)*22
        if ( b5 !=''):
            calories += int(b5)*50
        if ( b6!=''):
            calories += int(b6)*50
        if ( b7 !=''):
            calories += int(b7)*165
        if ( b8 !=''):
            calories += int(b8)*30
        if ( b9 !=''):
            calories += int(b9)*50
        if( b10 !=''):
            calories += int(b10)*45
        if ( b11 !=''):
            calories += int(b11)*22
        if ( b12 !=''):
            calories += int(b12)*45
        if ( b13!='' ):
            calories += int(b13)*320
        if ( b14 !=''):
            calories += int(b14)*80
        if ( b15!=''):
            calories += int(b15)*75
        if ( b16 !=''):
            calories += int(b16)*45
        if ( b17 !=''):
            calories += int(b17)*75
        if ( b18 !='' ):
            calories += int(b18)*80
            
        bv = True
        return HttpResponseRedirect('/lunch_dinner/')

def lunch_dinner(request):
    global calories, ldv
    if request.method == "GET":
        if ldv:
            return HttpResponseRedirect('/')
        return render(request,'countit/lunch_dinner.html')
    if request.method == "POST":
        ld1 = request.POST["ash reshteh"]
        ld2 = request.POST["ashe jo"]
        ld3 = request.POST["rice"]
        ld4 = request.POST["khorest fesenjan"]
        ld5 = request.POST["khorest bademjan"]
        ld6 = request.POST["khorest gheimeh"]
        ld7 = request.POST["khoresht karafs"]
        ld8 = request.POST["kashke bademjan"]
        ld9 = request.POST["halim bademjan"]
        ld10 = request.POST["Chicken breast"]
        ld11 = request.POST["ghormehsabzi"]
        ld13 = request.POST["drumsticks"]
        ld14 = request.POST["abgoosht"]
        ld15 = request.POST["vegetable soup"]
        ld16 = request.POST["barley soup"]
        ld17 = request.POST["kubideh kebab"]
        ld18 = request.POST["lasagna"]
        ld19 = request.POST["Cheese pizza"]
        ld20 = request.POST["vegetable Pizza"]
        ld21 = request.POST["kofteh Tabrizi"]
        ld22 = request.POST["fried shrimp"]
        ld23 = request.POST["French Fries"]
        ld24 = request.POST["Low fat yogurt"]
        ld25 = request.POST["Olivier salad"]
        ld26 = request.POST["fried fish"]
        if (ld1 !=''):
            calories += int(ld1)*261
        if (ld2!='' ):
            calories += int(ld2)*150
        if (ld3 !=''):
            calories += int(ld3)*35
        if (ld4 !=''):
            calories += int(ld4)*60
        if (ld5!=''):
            calories += int(ld5)*45
        if (ld6 !='' ):
            calories += int(ld6)*45
        if (ld7!='' ):
            calories += int(ld7)*45
        if (ld8 !='' ):
            calories += int(ld8)*50
        if (ld9 !='' ):
            calories += int(ld9)*50
        if (ld10 !=''):
            calories += int(ld10)*284
        if (ld11!='' ):
            calories += int(ld11)*45
        if (ld13!=''):
            calories += int(ld13)*109
        if (ld14 !='' ):
            calories += int(ld14)*150
        if (ld15!='' ):
            calories += int(ld14)*160
        if (ld16!=''):
            calories += int(ld16)*200
        if (ld17 !='' ):
            calories += int(ld17)*300
        if (ld18 !='' ):
            calories += int(ld18)*500
        if (ld19 !='' ):
            calories += int(ld19)*250
        if (ld20 !=''):
            calories += int(ld20)*200
        if (ld21 !=''):
            calories += int(ld21)*250
        if (ld22 !=''):
            calories += int(ld22)*1
        if (ld23!='' ):
            calories += int(ld23)*4
        if (ld24 !='' ):
            calories += int(ld24)*250
        if (ld25 !=''):
            calories += int(ld25)*60
        if (ld26 !=''):
            calories += int(ld26)*1
        ldv = True
        return HttpResponseRedirect('/snack/')
def snack(request):
    global calories, sv
    if request.method == "GET":
        if sv:
            return HttpResponseRedirect('/')
        return render(request, 'countit/snack.html')
    if request.method == "POST":
        s1 = request.POST["Pineapple"]
        s2 = request.POST["Apple"]
        s3 = request.POST["Pomegranate"]
        s4 = request.POST["Banana"]
        s5 = request.POST["Orange"]
        s6 = request.POST["Strawberry"]
        s7 = request.POST["Cantaloupe"]
        s8 = request.POST["Coconut water"]
        s9 = request.POST["Peach"]
        s10 = request.POST["Carrots"]
        s11 = request.POST["Figs"]
        s12 = request.POST["Raisins"]
        s13 = request.POST["Date"]
        s14 = request.POST["Watermelon"]
        s15 = request.POST["Peanut kernels"]
        s16 = request.POST["Pistachio"]
        s17 = request.POST["Walnut"]
        s18 = request.POST["Chips"]
        s19 = request.POST["Cheetos"]
        s20 = request.POST["Kranchi"]
        s21 = request.POST["Popcorn"]
        if (s1!=''):
            calories += int(s1)*453
        if (s2!=''):
            calories += int(s2)*95
        if (s3 !=''):
            calories += int(s3)*234
        if (s4 !=''):
            calories += int(s4)*111
        if (s5 !=''):
            calories += int(s5)*62
        if (s6 !=''):
            calories += int(s6)*14
        if (s7 !=''):
            calories += int(s7)*23
        if (s8 !=''):
            calories += int(s8)*4
        if (s9 !=''):
            calories += int(s9)*59
        if (s10 !=''):
            calories += int(s10)*25
        if (s11 !=''):
            calories += int(s11)*7
        if (s12 !=''):
            calories += int(s12)*3
        if (s13 !=''):
            calories += int(s13)*23
        if (s14 !=''):
            calories += int(s14)*50
        if (s15!=''):
            calories += int(s15)*6
        if (s16 !=''):
            calories += int(s16)*4
        if (s17 !=''):
            calories += int(s17)*26
        if (s18!=''):
            calories += int(s18)*6
        if (s19 !=''):
            calories += int(s19)*5000
        if (s20 !=''):
            calories += int(s20)*5000
        if (s21 !=''):
            calories += int(s21)*3870
        sv = True
        return HttpResponseRedirect('/drinks/')
def drinks(request):
    global calories, drv
    if request.method == "GET":
        if drv:
            return HttpResponseRedirect('/')
        return render(request, 'countit/drink.html')
    if request.method == "POST":
        dr1 = request.POST["Cherry juice"]
        dr2 = request.POST["pineapple juice"]
        dr3 = request.POST["Pomegranate juice"]
        dr4 = request.POST["mango juice"]
        dr5 = request.POST["Orange juice"]
        dr6 = request.POST["Apple juice"]
        dr7 = request.POST["Cantaloupe juice"]
        dr8 = request.POST["Coconut water"]
        dr9 = request.POST["Carrot juice"]
        dr10 = request.POST["Tea"]
        dr11 = request.POST["Beer"]
        dr12 = request.POST["Dough"]
        dr13 = request.POST["Soda"]
        dr14 = request.POST["Coffee"]
        dr15 = request.POST["Nescafé"]
        dr16 = request.POST["Milk"]
        dr17 = request.POST["Coffee Mix"]
        if (dr1 !=''):
            calories += int(dr1)*100
        if (dr2 !=''):
            calories += int(dr2)*105
        if (dr3 !=''):
            calories += int(dr3)*105
        if (dr4 !=''):
            calories += int(dr4)*120
        if (dr5 !=''):
            calories += int(dr5)*90
        if (dr6 !=''):
            calories += int(dr6)*100
        if (dr7 !=''):
            calories += int(dr7)*60
        if (dr8 !='' ):
            calories += int(dr8)*40
        if (dr9 !=''):
            calories += int(dr9)*80
        if (dr10 !=''):
            calories += int(dr10)*2
        if (dr11!=''):
            calories += int(dr11)*70
        if (dr12!=''):
            calories += int(dr12)*55
        if (dr13 !=''):
            calories += int(dr14)*110
        if (dr14!=''):
            calories += int(dr16)*110
        if (dr15 !=''):
            calories += int(dr17)*90
        drv = True
        return HttpResponseRedirect('/dessert/')

def dessert(request):
    global calories, dv, name, age, gender, weight
    if request.method == "GET":
        if dv:
            return HttpResponseRedirect('/')
        return render(request, 'countit/dessert.html')
    if request.method == "POST":
        d1 = request.POST["Lollipop"]
        d2 = request.POST["Gum"]
        d3 = request.POST["Baklava"]
        d4 = request.POST["Bamieh"]
        d5 = request.POST["Biscuit"]
        d6 = request.POST["creamy Biscuit"]
        d7 = request.POST["Gummi candy"]
        d8 = request.POST["Jelly"]
        d9 = request.POST["Sugar"]
        d10 = request.POST["SHirbrenj"]
        d11 = request.POST["SHolehzard"]
        d12 = request.POST["Porridge"]
        d13 = request.POST["Caramel Cream"]
        d14 = request.POST["Chocolate Cake"]
        d15 = request.POST["Cookie"]
        d16 = request.POST["candy"]
        d17 = request.POST["Apple Pie"]
        if (d1 !=''):
            calories += int(d1)*20
        if (d2 !=''):
            calories += int(d2)*5
        if (d3 !=''):
            calories += int(d3)*5
        if (d4 !=''):
            calories += int(d4)*80
        if (d5!=''):
            calories += int(d5)*20
        if (d6 !=''):
            calories += int(d6)*40
        if (d7 !=''):
            calories += int(d7)*3
        if (d8 !=''):
            calories += int(d8)*125
        if (d9 !=''):
            calories += int(d9)*20
        if (d10 !=''):
            calories += int(d10)*250
        if (d11 !=''):
            calories += int(d11)*250
        if (d12 !=''):
            calories += int(d12)*250
        if (d13 !=''):
            calories += int(d13)*4
        if (d14 !=''):
            calories += int(d14)*4
        if (d15 !=''):
            calories += int(d15)*5
        if (d16 !=''):
            calories += int(d16)*35
        if (d17 !=''):
            calories += int(d17)*150
        dv = True
        user = PersonalInformation.objects.create(
            name=name, age=age, weight=weight, gender=gender, calories=calories)
        output = {'data': user}
        name, age, weight, gender = '', '', '', ''
        calories = 0
        return render(request,'countit/result.html',context=output)

        


    

