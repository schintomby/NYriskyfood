# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError

class Facility(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	zipcode = models.CharField(max_length=10)
	county = models.CharField(max_length=50)
	lat_long = models.CharField(max_length=50) 

class Violation(models.Model):
	facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
	inspection_date = models.DateField()
	num_critical_violations = models.IntegerField(default=0)
	num_uncorrected_critical_violations = models.IntegerField(default=0)
	inspection_comments = models.CharField(max_length=500) 
	violation_description = models.CharField(max_length=500)

	def in_violation(self):
		return self.num_uncorrected_critical_violations > 0