from django.db import models

class ProcessorCharacteristics(models.Model):
    name = models.TextField()
    number_of_cores = models.PositiveSmallIntegerField()
    processor_technology = models.PositiveSmallIntegerField()
    base_clock = models.PositiveSmallIntegerField()
    thermal_design_power = models.PositiveSmallIntegerField()
    cache_memory = models.TextField()
    integrated_graphics_core = models.TextField()
    img = models.TextField()
    units_in_stock = models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField()
