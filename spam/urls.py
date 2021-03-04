from django.urls import path,include
from . import views
from django.conf.urls import url

# router = routers.DefaultRouter()
# router.register('spam_filter',views.SpamView)

urlpatterns = [
    path('<int:listing_id>',views.detect_spam,name='detect_spam'),]