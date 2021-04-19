from .models import CustomUser

def save_profile(backend,user,response, *args, **kwargs):
    if backend.name == "facebook":
        CustomUser.objects.filter(
            id=user.id, 
        ).update(photo_url=response['picture']['data']['url'])
    elif backend.name == "google-oauth2":
        CustomUser.objects.filter(
            id=user.id, 
        ).update(photo_url=response['picture'])