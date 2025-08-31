from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import PaymentsVievSet

app_name = UsersConfig.name

router = SimpleRouter()
router.register("", PaymentsVievSet)

urlpatterns = [] + router.urls
