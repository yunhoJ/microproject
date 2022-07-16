from django.urls import URLPattern, path
from .views import ShopViewSets, OrderViewSets

URLPatterns=[
    path('shop',ShopViewSets.as_view({
        'get':'list',
        "post":"create",
        
    })),
    path('shop/<str:pk>',ShopViewSets.as_view({
        'get':'retrieve',
        "put":"update",
        "delete":"destroy"
        
    })),
    path('order',ShopViewSets.as_view({
        'get':'list',
        "post":"create",
        
    })),
    path('order/<str:pk>',ShopViewSets.as_view({
        'get':'retrieve',
        "put":"update",
        "delete":"destroy"
        
    })),

]