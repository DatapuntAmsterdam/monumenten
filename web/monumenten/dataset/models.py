from django.contrib.gis.db import models

class Complex(models.Model):
    """
    Complex model
    -- aanvulling op stelselpedia --
    status:geeft [Rijksmomument, Gemeentelijk monument, Geen status] aan.
    """
    id = models.CharField(max_length=36, primary_key=True)

    beschrijving = models.TextField(null=True)
    monumentnummer = models.IntegerField(null=True)
    naam = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=128, null=True)

    def __str__(self):
        return "Complex {}".format(self.id)

class Monument(models.Model):
    """
    Monument model
    NOTE: 'geometrie' type is GeometryCollectionField, possibly in future (e.g. for searching)
    this needs to be split out in various Geometry types (POLYGON, MULTIPOLYGON, LINESTRING).
    """
    id = models.CharField(max_length=36, primary_key=True)

    aanwijzingsdatum = models.DateField(null=True)
    architect = models.CharField(max_length=128, null=True)
    beperking = models.IntegerField(null=True)
    beschrijving = models.TextField(null=True)
    coordinaten = models.PointField(null=True, srid=28992)
    complex= models.ForeignKey(Complex, related_name='monumenten', null=True)
    afbeelding = models.CharField(max_length=36, null=True)
    functie = models.CharField(max_length=128, null=True)
    geometrie = models.GeometryCollectionField(null=True, srid=28992)
    in_onderzoek = models.CharField(max_length=3, null=True)
    monumentnummer = models.IntegerField(null=True)
    naam = models.CharField(max_length=255, null=True)
    opdrachtgever = models.CharField(max_length=128, null=True)
    pand_sleutel = models.BigIntegerField(default=0)
    periode_start = models.IntegerField(null=True)
    periode_eind = models.IntegerField(null=True)
    redengevende_omschrijving = models.TextField(null=True)
    status = models.CharField(max_length=128, null=True)
    type = models.CharField(max_length=128, null=True)

    def __str__(self):
        return "Monument {}".format(self.id)




class Situering(models.Model):
    """
    Situering model
    -- aanvulling op stelselpedia --
    eerste_situering: geeft aan welke situering de eerste is.
    adresgegevens.
    """
    id = models.CharField(max_length=36, primary_key=True)

    betreft = models.IntegerField(null=True)
    situering_nummeraanduiding = models.CharField(max_length=128, null=True)
    eerste_situering = models.CharField(max_length=3, null=True)

    huisletter = models.CharField(max_length=1, null=True)
    huisnummer = models.IntegerField(null=True)
    nummeraanduiding = models.CharField(max_length=255, null=True)
    postcode = models.CharField(max_length=6,null=True)
    straat = models.CharField(max_length=80, null=True)
    toevoeging = models.CharField(max_length=4, null=True)

    def __str__(self):
        return "Complex {}".format(self.id)