.. _api:

=========================================
Adding Django Rest framework API endpoint
=========================================


Registering the API
===================

If you have installed Django REST framework, all you have to do is add categories router to your router:

.. code-block:: python

   from rest_framework.routers import DefaultRouter
   from categories.api.urls import router as category_router

   router = DefaultRouter()
   router.registry.extend(category_router.registry)
