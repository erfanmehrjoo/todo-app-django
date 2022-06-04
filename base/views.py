from django.shortcuts import render , HttpResponse , redirect
from django.urls import reverse_lazy
from .models import Task
from django.views.generic import CreateView , UpdateView , DeleteView , FormView , ListView , DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.
### make the authemtaecations system
class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('tasks')

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)

### task list
class TaskList(LoginRequiredMixin , ListView):
    model = Task
    template_name = 'list.html'
    context_object_name = 'tasks'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context



### make the list view
class TaskDetail(LoginRequiredMixin , DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'detail.html'

### task create
class TaskCreate(LoginRequiredMixin , CreateView):
    model = Task
    template_name = 'create'
    fields = ["title" , "descriptions" , "complete"]
    template_name = 'create.html'
    success_url = reverse_lazy('tasks')

    def form_valid(self , form):
        form.instance.user = self.request.user
        return super(TaskCreate , self).form_valid(form)

class TaskUpdate(LoginRequiredMixin , UpdateView):
    model = Task
    fields = ["title" , "descriptions" , "complete"]
    template_name = 'update.html'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskUpdate , self).form_valid(form)
    
class TaskDelete(LoginRequiredMixin , DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('tasks')
