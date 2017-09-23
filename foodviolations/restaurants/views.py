# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from restaurants.models import Violation
from django.db.models import Q
import re

def strReplace(pattern,datastr):
    # searches for strings to highlight before sending back to search results
    matchpos = datastr.lower().find(pattern.lower())
    if(matchpos!=-1):
        # need to highlight 1 or more strings... use the parenthesis to inlcude the delimiter when string is tokenized
        my_regex = r"(" + re.escape(pattern) + r")(?i)"
        segments = re.split(my_regex, datastr, flags=re.IGNORECASE)
        finalStr = ""
        for index, seg in enumerate(segments):
        	# for every instance of the string, wrap it in a highlight class and retain its case
            if seg.lower() == pattern.lower():
            	finalStr = "%s%s%s%s" % (finalStr,"<div class=\"highlight\">",seg,"</div>")
            else:
                finalStr = "%s%s" % (finalStr,seg)	
        # finished concatenating the segments, return the new string
        return finalStr
    else:
    	return datastr # no string was found, return unlatered string 
    
    

def index(request):
    # determine if a search was performed
    searchStr = request.GET.get('searchStr')
    if(searchStr):
        violations = Violation.objects.filter(num_uncorrected_critical_violations__gt = 0).order_by('facility__county')
        violations = violations.filter(Q(violation_description__icontains=searchStr) 
        	| Q(inspection_comments__icontains=searchStr) 
        	| Q(facility__name__icontains=searchStr)
        	| Q(facility__city__icontains=searchStr)
        	| Q(facility__address__icontains=searchStr)
        	| Q(facility__county__icontains=searchStr))
        for v in violations:
        	# highlight any matched strings to description
        	highlightedStr = strReplace(searchStr, v.violation_description)
        	v.violation_description = highlightedStr
        	# highlight any matched strings to inspector comments
        	highlightedStr = strReplace(searchStr, v.inspection_comments)
        	v.inspection_comments = highlightedStr
        	# highlight any matched strings to facility name
        	highlightedStr = strReplace(searchStr, v.facility.name)
        	v.facility.name = highlightedStr
        	# highlight any matched strings to facility address
        	highlightedStr = strReplace(searchStr, v.facility.address)
        	v.facility.address = highlightedStr
        	# highlight any matched strings to facility city
        	highlightedStr = strReplace(searchStr, v.facility.city)
        	v.facility.city = highlightedStr
        	# highlight any matched strings to facility county
        	highlightedStr = strReplace(searchStr, v.facility.county)
        	v.facility.county = highlightedStr
    	return render(request, "index.html",
            	{"violations": violations, 'searchStr': searchStr })
    else:
        # no search was performed, send back a complete list
        violations = Violation.objects.filter(num_uncorrected_critical_violations__gt = 0).order_by('facility__county')
        context = {
	        'violations': violations
	    }
        return render(request, 'index.html', context)





