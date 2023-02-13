from rest_framework import viewsets
from blog.serializers import ImagesSerializer
from blog.models import Images, Profile
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from django.contrib.auth.models import User

class ImagesViewSet(viewsets.ModelViewSet):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

    def get_queryset(self):

        user = self.request.user
        filtered = Images.objects.filter(author=user) #oczekiwana wartość to numer id (integer) np author=1 lub author =2 // aktualnie zalogowany user >> author=user zwraca numer id aktualnie zalogowanego usera

        return filtered





print('\n\n')


#print(Profile.objects.filter(id=1))
#user_obj = User.objects.filter(id=2).first()
#profile_obj = Profile.objects.all().first()
#print(profile_obj.membership)
#print(profile_obj.user)
#print(user_obj == profile_obj.user)


filtered = Images.objects.filter(author=2)

print(filtered)



print('\n\n')