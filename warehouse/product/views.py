from django.shortcuts import render,redirect
from user.models import All_categories,Categories,Product
from product.forms import AllCategoriesForm , CategoriesForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def product_home(request):
    all_categories=All_categories.objects.all().order_by('name')
    
    context={'all_categories':all_categories,}
    return render(request,'product/product_home.html',context)

@login_required(login_url='/login/')
def add_categories(request):
    if request.method != 'POST':
        form=AllCategoriesForm()
    else:
        form=AllCategoriesForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect ('product:product_home')
    context={'form':form}
    return render(request,'product/add_all_categories.html',context)


@login_required(login_url='/login/')
def Categories(request,categories_id):
    all_categoriess=All_categories.objects.get(id=categories_id)
    categories=all_categoriess.categories_set.order_by('name')
    context={ 'all_categoriess':all_categoriess,'categories':categories }
    return render(request,'product/categories.html',context)


@login_required(login_url='/login/')
def product(request,product_id):
    categories=Categories.objects.get(id=product_id)
    product=categories.product_set.order_by('name')
    context={'categories':categories,'product':product}
    return render(request,'product/product.html',context)


@login_required(login_url='/login/')
def add_categories2(request):
    if request.method != 'POST':
        form=CategoriesForm()
    else:
         form=CategoriesForm(data=request.POST)
         if form.is_valid():
             form.save()
             return redirect('')
    context={'form':form}
    return render(request,'product/add_categories2.html',context)

@login_required(login_url='/login/')
def update(request,all_categories_id):
    all_categories=All_categories.objects.get(id=all_categories_id)
    context={'all_categories':all_categories}
    return render(request,'product/update.html',context)

                                                                                                              