"""explorer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from explorer.views import Callback, Home
from apps.monzo.views import (
    MerchantView,
    MerchantTagsUpdate,
    TransactionView,
    TransactionNoteUpdate,
    TransactionTagsUpdate,
    TransactionReviewedUpdate,
    TransactionsMonthView,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', Home.as_view(), name='homepage'),
    path('callback', Callback.as_view(), name='callback'),

    path(
        '<int:year>/<int:month>/',
        TransactionsMonthView.as_view(month_format='%m'),
        name='transactions_month',
    ),
    path(
        'transactions/<str:pk>/',
        TransactionView.as_view(),
        name='transaction',
    ),
    path(
        'transactions/<str:pk>/note',
        TransactionNoteUpdate.as_view(),
        name='transaction_note',
    ),
    path(
        'transactions/<str:pk>/tags',
        TransactionTagsUpdate.as_view(),
        name='transaction_tags',
    ),
    path(
        'transactions/<str:pk>/reviewed',
        TransactionReviewedUpdate.as_view(),
        name='transaction_reviewed',
    ),

    path(
        'merchants/<str:pk>/',
        MerchantView.as_view(),
        name='merchant',
    ),
    path(
        'merchants/<str:pk>/tags',
        MerchantTagsUpdate.as_view(),
        name='merchant_tags',
    ),
]
