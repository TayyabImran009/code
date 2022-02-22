
from typing import Tuple
from django.db import models
from django.db.models.base import Model
from .utils import *
from paranoid_model.models import Paranoid
from django.core.validators import MaxValueValidator, MinValueValidator 
import uuid


# Create your models here.
class BaseModel(Paranoid):
	uuid = models.UUIDField(default=uuid.uuid4, unique=True)

	class Meta:
		abstract = True


class Vat(BaseModel):
	description = models.CharField(max_length=10, blank=True, null=True)
	amount = models.FloatField(default=0)
	def __str__(self):
		return self.description
	class Meta:
		verbose_name = "Vat"
		verbose_name_plural = "Vat"


class Cost(BaseModel):
	description = models.CharField(max_length=50)
	amount = models.FloatField(null=False)
	active = models.BooleanField(default=False, blank=False)
	# vat = models.ForeignKey(Vat, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.description)
	class Meta:
		verbose_name = "Cost"
		verbose_name_plural = "Cost"


class CostQuantity(BaseModel):
	# cost = models.ForeignKey(Cost, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
	amount = models.FloatField(blank=True, null=False)

	def __str__(self):
		return str(self.amount)
	class Meta:
		verbose_name = "Cost Quantity"
		verbose_name_plural = "Cost Quantity"


class Validation(BaseModel):
	calculation_type = models.IntegerField(choices=CALCULATION_TYPES)
	reference = models.CharField(max_length=15)
	make = models.CharField(max_length=25, blank=True, null=True)
	model = models.CharField(max_length=50)
	amount_purchase = models.FloatField()
	purchase_vat = models.BooleanField(default=False)
	amount_sale = models.FloatField()
	sale_vat = models.BooleanField(default=False)
	margin = models.FloatField(blank=True, null=True)
	type = models.IntegerField(choices=VEHICLE_TYPES)
	risk = models.IntegerField(choices=VEHICLE_RISKS)
	# costs = models.ManyToManyField(CostQuantity)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.reference
	class Meta:
		verbose_name = "Validation"
		verbose_name_plural = "Validation"
