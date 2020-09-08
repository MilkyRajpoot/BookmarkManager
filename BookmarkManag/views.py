from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView # API data
from rest_framework.response import Response # Successful 200 response
from rest_framework import status # send back status
from  .models import * # import all DB
from . serializers import * # import all serializer
from . forms import * # import all forms
from django.db.models import Q
from rest_framework import generics
from rest_framework import filters # DRF Filter 
import pdb # For Debugging
import json
import datetime
import pytz

# Create api endpoint -- /_api/create -- which allows storing of any Customer's bookmark
class BookmarkApi(APIView):

	def get(self, request):
		bookmark_list=Bookmark.objects.all()
		serializer=bookmarkSerializer(bookmark_list,many=True)
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
	 	bookmark_serializer = bookmarkSerializer(data=request.data)
	 	if bookmark_serializer.is_valid():
	 		bookmark_serializer.save()
	 		return Response(bookmark_serializer.data, status=status.HTTP_201_CREATED)
	 	else:
	 		return Response(bookmark_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create another api endpoint - /_api/browse -- which allows browsing and filtration of API endpoint with the following query parameters: 
class BookmarkListView(generics.ListAPIView):
    queryset = CustomerBookmark.objects.all()
    serializer_class = browsecusbookSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['bookmark__title']
    # filter_backends = []
    ordering_fields = ['created_at','id','updated_at']


# (Create) Assign Bookmark and Customer new Data with api endpoint - /_api/searchApi -- which allows assigning Customer's Bookmark to Customer Pofile of API: 
class BookmarkBrowseApi(APIView):

	def post(self, request, *args, **kwargs):
	 	cusbook_serializer = cusbookSerializer(data=request.data)
	 	if cusbook_serializer.is_valid():
	 		cusbook_serializer.save()
	 		return Response(cusbook_serializer.data, status=status.HTTP_201_CREATED)
	 	else:
	 		return Response(cusbook_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create and Get Customer Profile Data via below API's
class CustomerProApi(APIView):

	def get(self, request):
		cusPro_list=Customer.objects.all()
		serializer=customerSerializer(cusPro_list,many=True)
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
	 	cusPro_serializer = customerSerializer(data=request.data)
	 	if cusPro_serializer.is_valid():
	 		cusPro_serializer.save()
	 		return Response(cusPro_serializer.data, status=status.HTTP_201_CREATED)
	 	else:
	 		return Response(cusPro_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def create(request):
    form = BookmarkForm(request.POST,request.FILES)
    template = "create.html"
    context = {"form": form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/_api/home/")
    else: 
        form = BookmarkForm()   
    return render(request, template, context)

def createCus(request):
    form = CustomerForm(request.POST,request.FILES)
    template = "create.html"
    context = {"form": form}
    if request.method == 'POST':
	    if form.is_valid():
	        obj = form.save(commit=False)
	        obj.save()
	        return HttpResponseRedirect("/_api/home/")
	    else: 
	        form = CustomerForm()   
    return render(request, template, context) 

def createCusBook(request):
    form = CustomerBookmarkForm(request.POST,request.FILES)
    template = "create.html"
    context = {"form": form}
    if request.method == 'POST':
	    if form.is_valid():
	        obj = form.save(commit=False)
	        obj.save()
	        return HttpResponseRedirect("/_api/home/")
	    else: 
	        form = CustomerBookmarkForm()   
    return render(request, template, context)

def list_viewData(request): 
    obj = CustomerBookmark.objects.all().values()
    # print(obj)
    context = {"object_list" : obj}
    template = "allDataList.html"    
    return render(request, template, context)

def details_view(request, customer_id=None, bookmark_id=None): 
    objBook = get_object_or_404(Bookmark, id=bookmark_id)
    objCus = get_object_or_404(Customer, id=customer_id)
    print(objBook,objCus)
    context = {
    		"object_cus" : objCus,
    		"object_book" : objBook,
    		}
    template = "getData.html"    
    return render(request, template, context)