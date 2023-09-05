from django.db import models


class VehicleType(models.Model):
    type = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.type


class StatusRegister(models.Model):
    status = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.status


class StatusCustomer(models.Model):
    status = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.status


class InputRegister(models.Model):
    placa = models.CharField(max_length=6, primary_key=True)
    input = models.DateTimeField()
    output = models.DateTimeField(null=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusRegister, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.placa, self.final_price, self.vehicle_type_id, self.status_id}"
