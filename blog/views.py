from django.forms import BaseModelForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, AddCommentForm
from django.http import HttpResponse, HttpResponseRedirect

class HomeView(ListView):
    """Displays articles on homepage."""
    model = Post
    template_name = 'blog.html'
    ordering = ['-date']


class PostDetailView(DetailView):
    """Displays a an article in detail."""
    model = Post
    template_name = 'post.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        var = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = var.total_likes()

        liked = False
        if var.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["category_menu"] = category_menu 
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
        

class AddPostView(CreateView):
    """Displays form to post an article."""
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCommentView(CreateView):
    """Displays form to post a comment."""
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_comment.html'
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article', kwargs={'pk':self.kwargs['pk']})


class EditPostView(UpdateView):
    """Displays form to edit an article."""
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'


class DeletePostView(DeleteView):
    """Deletes an article."""
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('Home')


class AddCategoryView(CreateView):
    """Adds categories."""
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class EditCategoryView(UpdateView):
    """Edits categories"""
    model = Category
    form_class = EditForm
    template_name = 'edit_post.html'

def CategoryPageView(request, category):
    """Displays articles under a category."""
    category_posts = Post.objects.filter(category=category)
    return render(request, 'categories.html', {'category': category, 'category_posts': category_posts})

def CategoryListView(request):
    """Displays list of categories."""
    category_list = Category.objects.all()
    return render(request, 'category_list.html', {'category_list': category_list})

def LikeView(request, pk):
    """Allows user to like and unlike post."""
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))
    