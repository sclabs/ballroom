from django.contrib import admin
import models

ballroom_models = [
    models.Level,
    models.Style,
    models.Dance,
    models.Position,
    models.Figure,
    models.Routine,
    models.Video,
    models.Profile,
    models.FigureInstance,
    models.Annotation
]

admin.site.register(ballroom_models)
