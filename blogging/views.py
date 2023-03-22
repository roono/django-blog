from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader

from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.


class PostListView(ListView):
    model = Post.objects.exclude(published_date=None)
    queryset = model.order_by("-published_date")
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"

    def detail_view(self, request, post_id):
        post = self.get_object(pk=post_id)
        context = {"object": post}
        return render(request, "blogging/detail.html", context)
