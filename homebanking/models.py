# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuditoriaCuenta(models.Model):
    old_id = models.IntegerField(blank=True, null=True)
    new_id = models.IntegerField(blank=True, null=True)
    old_balance = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    new_balance = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    old_iban = models.CharField(blank=True, null=True)
    new_iban = models.CharField(blank=True, null=True)
    old_type = models.CharField(blank=True, null=True)
    new_type = models.CharField(blank=True, null=True)
    user_action = models.CharField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auditoria_cuenta'

class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    id_tarjeta = models.IntegerField()
    brand = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'marca'


class Movimientos(models.Model):
    numero_cuenta = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    tipo_operacion = models.CharField(blank=True, null=True)
    hora = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'movimientos'
