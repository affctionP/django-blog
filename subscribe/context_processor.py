from .forms import SubForm
from posts.models import Category ,PostModel
from posts.forms import searchForm

def inject_form(request):
    return {'form':SubForm()}

def base(request):
    cats = Category.objects.all()
    return{ 'cats':cats }

def searching(request):
    return {'searchform':searchForm()}

def newPosts(request):
    
    new_Posts = PostModel.objects.filter(status ='p').order_by('-publish')[:2]
    return {'newPosts':new_Posts}
def Hot_Post(request):
    hot = PostModel.objects.filter(status='p').order_by('views')
    

        