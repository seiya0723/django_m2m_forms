from django.shortcuts import render,redirect

from django.views import View
from .models import Menu,Category,Allergy
from .forms import MenuForm

class MenuView(View):

    def get(self, request, *args, **kwargs):

        cates   = Category.objects.all()
        alles   = Allergy.objects.all()
        form    = MenuForm()

        data    = Menu.objects.order_by("category")
        context = { "data":data,
                    "form":form,
                    "cates":cates,
                    "alles":alles }

        return render(request,"menulist/index.html",context)
    
    def post(self, request, *args, **kwargs):

        form    = MenuForm(request.POST)

        if form.is_valid():
            print("バリデーションOK")
            form.save()
            
        else:
            print("バリデーションNG")



        return redirect("menulist:index")


index   = MenuView.as_view()
