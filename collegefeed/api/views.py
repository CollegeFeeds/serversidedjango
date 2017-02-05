from django.shortcuts import render
from django.http import HttpResponse
from api.models import mphilresults,mphilcounters,undergradresults,undergradcounters,postgradresults,postgradcounters,ncwebresults,ncwebcounters,diplomaresults,diplomacounters
import json

# Create your views here.
  
################# API FUNCTION FOR RESULTS ######
# A dictionary for result category used akin to switch case in this case
result_counterdict={
	'1':mphilcounters,
	'2':undergradcounters,
	'3':postgradcounters,
	'4':diplomacounters,
	'5':ncwebcounters
}
result_resultsdict={
	'1':mphilresults,
	'2':undergradresults,
	'3':postgradresults,
	'4':diplomaresults,
	'5':ncwebresults
}
def results(request,category):
	print category
	global result_counterdict
	category_counter=result_counterdict[category]
	global result_resultsdict
	category_result=result_resultsdict[category]
	print category_counter,category_result
	start_index=request.GET.get("from")
	end_index=request.GET.get("to")
	current_indexindb=category_counter.objects.all()[0].mphilid - 6
	index_range=int(end_index)-int(start_index)
	queryset=category_result.objects.filter(id__range=(current_indexindb-int(end_index),current_indexindb-int(start_index))).values()
	responseDict={}
	for i in range(len(queryset)):
		responseDict[i+1]=queryset[i];

	jsonResponse=json.dumps(responseDict,indent=4)
	return HttpResponse(jsonResponse,content_type="application/json")

##################### END OF RESULT API #################

