from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Deep



ocean_dict = {
    'Pacific': 'Ти́хий океа́н — самый большой по площади и глубине океан на Земле.',
    'Atlantic': 'Атланти́ческий океа́н — второй по величине и глубине океан Земли.',
    'Indian': 'Инди́йский океа́н — третий по площади и глубине океан Земли',
    'Arctic': 'Се́верный Ледови́тый океа́н — наименьший по площади и глубине океан Земли'
}
hemi_dict = {
    'Океаны Северного Полушария':'Arctic',
    'Океаны Южного Полушария':'Pacific, Atlantic, Indian'
}

def index(request):
    ocean_keys_list = list(ocean_dict)

    context = {
     "var2keyslist":ocean_keys_list
    }
    return render(request, 'oceansapp/index.html', context=context)

def get_info_number(request, water:int):
    ocean_keys_list = list(ocean_dict)
    if water > len(ocean_keys_list):
        return HttpResponse(f"Автор данного сайта считает что океана всего 4. Введите номер океана в зависимости от площади. Неправильный номер {water}")
    name_ocean = ocean_keys_list[water-1]
    redirect_url = reverse("oceansapp_name", args=(name_ocean,))
    return HttpResponseRedirect(redirect_url)

def get_info(request, water:str):
    ocean_values = ocean_dict.get(water)
    data = {
        "var1info":ocean_values
    }
    return render(request, 'oceansapp/ocean.html', context=data)


def put_to_hemishere(request):
    base = {
        "var3hemi_dict":hemi_dict
    }

    return render(request, "oceansapp/dict.html", context=base)


def get_hemishere(request, hemishere):

    if hemishere == "north":
        N_list = hemi_dict['north']


        return HttpResponse(N_list)
    elif hemishere == "south":
        S_list = hemi_dict['south']
        return HttpResponse(S_list)
    else:
        return HttpResponseNotFound(f"Нет такого полушария {hemishere}")


def get_deep(request):
    modeldeeptable = Deep.objects.all()
    return render(request, "oceansapp/deep.html", {"modeldeeptable":modeldeeptable})

def get_deepone(request, int_deepone:int):
    deepone = get_object_or_404(Deep, id=int_deepone)
    return render(request, "oceansapp/deepone.html", {"deepone":deepone})




def get_hemi(request):
    return render(request, "oceansapp/new.html", {})





