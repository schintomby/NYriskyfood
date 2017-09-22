import csv
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","foodviolations.settings")
import django
django.setup()

from restaurants.models import Facility, Violation

def fetch_facilities():
	# time to open the data file, import into sqlite
    with open("Food_Service_Establishment__Last_Inspection.csv") as f:
    	recs = csv.DictReader(f)
    	for rec in recs:
            if rec["TOTAL # CRITICAL VIOLATIONS"] != "" and int(rec["TOTAL # CRITICAL VIOLATIONS"]) > 0:
	    		f = Facility(
	                name = rec["FACILITY"],
		            address =  rec["FACILITY ADDRESS"],
		            city =  rec["CITY"],
		            zipcode =  rec["ZIP CODE"],
		            county = rec["COUNTY"],
		            lat_long =  rec["Location1"],
	    		)
	    		f.save()

	    		vdate = rec["LAST INSPECTED"].split("/")
	    		v = Violation(
	    			facility =  f,  # set the foreign key
	    			# convert original format to django date field required format of YYYY-MM-DD 
		            inspection_date = "-".join([vdate[2],vdate[0],vdate[1]]), 
		            num_critical_violations = rec["TOTAL # CRITICAL VIOLATIONS"],
		            num_uncorrected_critical_violations = rec["TOTAL #CRIT.  NOT CORRECTED "],
		            inspection_comments = rec["INSPECTION COMMENTS"], 
		            violation_description = rec["VIOLATIONS"]
	    		)
	    		v.save()
	    		print f.name + " was inserted"
fetch_facilities()

