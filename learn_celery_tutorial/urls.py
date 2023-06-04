from django.urls import path
from .views import *

urlpatterns = [
    path('theory', LearnTheoryView.as_view(), name = LearnTheoryView.view_name),
    path('configuration-steps', ConfigurationStepsView.as_view(), name = ConfigurationStepsView.view_name),
    path('add-number', AddNumberCeleryTaskView.as_view(), name = AddNumberCeleryTaskView.view_name),
    path('check_task_status/', CheckTaskStatusView.as_view(), name = CheckTaskStatusView.view_name),
    path('number-counter-periodic-scheduled-task', NumberCounterPeriodicCeleryBeatScheduledTaskView.as_view(),name = NumberCounterPeriodicCeleryBeatScheduledTaskView.view_name),
    path('get-counter-number-from-cache/', GetCounterNumberFromCacheView.as_view(), name = GetCounterNumberFromCacheView.view_name),
    path('one-time-task/', OneTimeTaskView.as_view(), name = OneTimeTaskView.view_name),
]