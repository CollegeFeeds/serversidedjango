from django.shortcuts import render
from django.http import HttpResponse
from api.models import mphilresults,mphilcounters,undergradresults,undergradcounters,postgradresults,postgradcounters,ncwebresults,ncwebcounters,diplomaresults,diplomacounters
import json

# Create your views here.
  
################# API FUNCTION FOR RESULTS ######
def results(request):
	start_index=request.GET.get("from")
	end_index=request.GET.get("to")
	current_indexindb=mphilcounters.objects.all()[0].mphilid - 6
	index_range=int(end_index)-int(start_index)
	queryset=mphilresults.objects.filter(id__range=(current_indexindb-int(end_index),current_indexindb-int(start_index))).values()
	responseDict={}
	for i in range(len(queryset)):
		responseDict[i+1]=queryset[i];

	jsonResponse=json.dumps(responseDict,indent=4)
	return HttpResponse(jsonResponse,content_type="application/json")

