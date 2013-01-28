from django.db import models

class CoolModel ( Model ):
        class Meta:
                abstract = True
                app_label = "db"
        def __init__ ( self, *args, **kwargs ):
                super(CoolModel, self).__init__(*args, **kwargs)
                self.__initial = self._dict
        def toDict ( self, properties = "*" ):
                def getValue ( field, properties = "*" ):
                        value = getattr(self, field.name)
                        if isinstance(field, ForeignKey):
                                if field.name in properties:
                                        return value.toDict(properties[field.name])
                        elif isinstance(value, datetime.date) or isinstance(value, datetime.datetime):
                                return value.isoformat()
                        elif isinstance(field, CommaSeparatedIntegerField) and isinstance(value, basestring):
                                return json.loads(value)
                        elif isinstance(value, Decimal):
                                return float(value)
                        elif isinstance(field, ImageField):
                                return value.url if value else None
                        elif isinstance(field, NullBooleanField):
                                return None if value not in (True, False) else 1 if value else 0
                        else:
                                return value

                result = {}
                fields = {}
                for field in self._meta.fields:
                        fields[field.name] = field
                        if isinstance(field, ForeignKey):
                                idAttr = "%s_id" % field.name
                                result[idAttr] = getattr(self, idAttr)
                        else:
                                result[field.name] = getValue(field, properties)
                if isinstance(properties, dict):
                        for k, v in properties.iteritems():
                                if hasattr(self, k):
                                        value = getattr(self, k)
                                        if isinstance(value, CoolModel):
                                                result[k] = value.toDict(v)
                                        elif value.__class__.__name__ == "RelatedManager":
                                                result[k] = toJSON(value.all(), v)
                                        elif value is None:
                                                result[k] = {} if k in fields and isinstance(fields[k], ForeignKey) else None
                                        else:
                                                result[k] = value
                return result

        @property
        def diff ( self ):
                d1 = self.__initial
                d2 = self._dict
                diffs = [(k, (v, d2[k])) for k, v in d1.items() if v != d2[k]]
                return dict(diffs)

        @property
        def original ( self ):
                try:
                        return self.__class__.objects.get(id = self.id)
                except self.__class__.DoesNotExist:
                        return None

        @property
        def hasChanged ( self ):
                return bool(self.diff)

        @property
        def changedFields ( self ):
                return self.diff.keys()

        def getFieldDiff ( self, field_name ):
                return self.diff.get(field_name, None)

        def save ( self, *args, **kwargs ):
                super(CoolModel, self).save(*args, **kwargs)
                self.__initial = self._dict

        @property
        def _dict ( self ):
                return model_to_dict(self, fields = [field.name for field in self._meta.fields])


class Part_Types(models.CoolModel):
	name = models.CharField(max_length=30)


class Parts(models.CoolModel):
	number = models.CharField(max_length=3)
	part_type = models.ForeginKey(Part_Types)
	create_date = models.DateTimeField()
	last_modify_date = models.DateTimeField()
