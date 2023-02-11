from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)

from django.contrib.auth.forms import UserCreationForm


##################################################################


class HomeView(TemplateView):
    template_name = 'blog/home.html'                       


class OgloszeniaListView(ListView):
    model = Post                                                   
    template_name = 'blog/ogloszenia.html'      # (error domyslna nazwa templatu post_list)  <app>/<model>_<viewtype>.html
    context_object_name = 'posts'                               # domyslna nazwa obiektu to'object'
    ordering = ['-date_posted'] 
    paginate_by =10


#def home(request):                                           # <----------
#    context = {
#        'posts': Post.objects.all().order_by('-date_posted')                         
#    }
#    return render(request, 'blog/home.html', context)

##################################################################


class UserPostListView(ListView):
    model = Post                                              # <----------
    template_name = 'blog/user_posts.html'                          # blog/post_list.html (error domyslna nazwa templatu post_list)  <app>/<model>_<viewtype>.html
    context_object_name = 'posts'                             # domyslna nazwa obiektu to'object'
    #ordering = ['-date_posted']                               # - zmiana kolejności
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):                             # Zachowane domyślne nazwy (w tamplacie nazwa zmiennej object)
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):         # Zachowane domyślne nazwy
    model = Post                                              # Dla Create oczekiwana nazwa obiektu to 'form'
    fields = ['title', 'content']                             # LoginRequiredMixin nowe posty tylko przez zalogowanych
    
    def form_valid(self, form):                               # Your PostCreateView creates instances of Post and you have set fields = ['title','content'] meaning only these fields would show up in the form. 
        form.instance.author = self.request.user              # But you have a field author which is non-nullable and without a default, hence you need to set a value for this field too.
        messages.success(self.request, f'Post Successfully Created!')            
        return super().form_valid(form)                       # If you want to set it to the current logged in user you can override the form_valid method of the form and do it there

    def get_success_url(self):                                # dodatkowo stworzyć metode get_absolute_url w models.py aby przekierować do strony nowego posta      
        return reverse('blog-home')                           # lub tutaj metode get_success_url aby przekierowac do str głównej >>  bo wywala błąd o przekierowaniu


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):   # Używa tego samego tamplatu co PostCreateView , dodatkowo UserPassesTestMixin aby edycja tylko przez autora posta
    model = Post 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Post Updated!')      # w modelu należy dodać self.request! pamiętać o tym!
        return super().form_valid(form)

    def test_func(self):                                      # Sprawdzenie czy osoba chcąca edytować jest autorem
        post = self.get_object()
        return self.request.user == post.author               # Można zrobić z if self.request.user == post.author: return True, else: False

    def get_success_url(self):
        return reverse('blog-home')


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    #success_url = '/'                                         # Wystarczy success = '<adres_strony>' zamiast metody get_success_url
        
    def test_func(self):                                      # Sprawdzenie czy osoba chcąca usunąć jest autorem.
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    def get_success_url(self):
        messages.success(self.request, f'Post Deleted!')
        return reverse('blog-home')


def search(request):
    if request.method == 'POST':
        wyszukanie = request.POST['input_name']
        wyniki = Post.objects.filter(content__contains=wyszukanie)   # xxx__contains=wyszukanie   (xxx=np title z modelu Post, moze być content itd)

        return render(request, 'blog/search.html', 
            {'wyszukanie': wyszukanie,
            'wyniki': wyniki})

    return render(request, 'blog/search.html')


class CvView(TemplateView):
    template_name = 'blog/cv.html'





