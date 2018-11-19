from django.shortcuts import render, redirect
from .models import dairyNode
from  django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import dairyForm,searchForm
from django.contrib.auth import logout, login
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
# Create your views here.
def homePage(request):
	return render(request, 'homepage.html')

@login_required
def milkList(request):
	if request.user.is_superuser:
		milks = dairyNode.objects.all().order_by('-Date')
	else:
		milks = dairyNode.objects.filter(Name__username=request.user).order_by('-Date')
	page = request.GET.get('page')
	paginator = Paginator(milks, 6)
	try:
		milkss = paginator.get_page(page)
	except PageNotAnInteger:
		milkss = paginator.get_page(1)
	except EmptyPage:
		milkss = paginator.get_page(paginator.numbers)
	context = {'milk':milkss}
	return render(request, 'milklist.html',context)

@login_required
def addMilk(request):
	if request.method == 'POST':
		form = dairyForm(request.POST)
		if form.is_valid():
			milk = form.save(commit=False)
			milk.Name = request.user
			milk.save()
			return redirect('dairy:milklist')
	else:
		form = dairyForm()
	return render(request, 'addmilk.html', {'form':form})

@login_required
def searchFilter(request):
	if request.method == 'POST':
		form = searchForm(request.POST)
		if form.is_valid():
			selected_date = form.cleaned_data['Date']
			selected_node = form.cleaned_data['Node']
			searchByday = 	form.cleaned_data['search_by_day']
			if selected_node is not "" and searchByday is True:
				milks = dairyNode.objects.filter(Date__year=selected_date.year,Date__month=selected_date.month,Date__day=selected_date.day).filter(Name__username__icontains=selected_node).order_by('-Date')
			elif selected_node is "" and searchByday is True:
				milks = dairyNode.objects.filter(Date__year=selected_date.year,Date__month=selected_date.month,Date__day=selected_date.day).order_by('-Date')
			elif selected_node is not "" and searchByday is False:
				milks = dairyNode.objects.filter(Name__username__icontains=selected_node).order_by('-Date')
			# page = request.GET.get('page')
			# paginator = Paginator(milks, 6)
			# try:
			# 	milkss = paginator.get_page(page)
			# except PageNotAnInteger:
			# 	milkss = paginator.get_page(1)
			# except EmptyPage:
			# 	milkss = paginator.get_page(paginator.numbers)
			context ={'milk':milks}
			return render(request,'searchlist.html',context)
	else:
		form = searchForm()
	return render(request, 'searchform.html', {'form':form})

def logoutView(request):
	logout(request)
	return HttpResponseRedirect(reverse('dairy:home'))