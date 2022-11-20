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


    @staticmethod
    def core_filter(list):
        if len(list) == 0 or len(list) == 2:
            return ProcessorCharacteristics.objects.all()
        else:
            return ProcessorCharacteristics.objects.filter(integrated_graphics_core__contains=list[0])


    @staticmethod
    def pack_filter(list):
        if len(list) == 0 or len(list) == 2:
            return ProcessorCharacteristics.objects.all()
        else:
            return ProcessorCharacteristics.objects.filter(name__contains=list[0])


    @staticmethod
    def name_filter(list):
        if len(list) == 0:
            return ProcessorCharacteristics.objects.filter(name__contains = 'None')
        result = ProcessorCharacteristics.objects.filter(name__contains=list[-1])
        list.pop(-1)
        return result | ProcessorCharacteristics.name_filter(list)
