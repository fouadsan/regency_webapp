from .models import BlogModel, CommentModel
from .forms import *
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from main.models import Section

def BlogListView(request):
    dataset = BlogModel.objects.all()
    sections = Section.objects.all()
    recent_posts = BlogModel.objects.all()[:3]
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            dataset = BlogModel.objects.filter(blog_title__icontains=form['title'].value())
    else:
        form = SearchForm()

    if request.method == 'GET' and 'section' in request.GET:
        section_search = SectionSearch(request.GET)
        section = section_search['section'].value()
        dataset = BlogModel.objects.filter(section_id=section)
    else:
        section_search = SectionSearch()
    paginator = Paginator(dataset, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'sections': sections,
        'page_obj': page_obj,
        'recent_posts': recent_posts,
        'form': form,
    }
    return render(request, 'blog/listview.html', context)


def BlogDetailView(request, _id):
    try:
        data = BlogModel.objects.get(id=_id)
        comments = CommentModel.objects.filter(blog=data)
    except BlogModel.DoesNotExist:
        raise Http404('Data does not exist')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = CommentModel(your_name=form.cleaned_data['your_name'],
                                   comment_text=form.cleaned_data['comment_text'],
                                   blog=data)
            Comment.save()
            return redirect(f'/blogs/blog/{_id}')
    else:
        form = CommentForm()

    context = {
        'data': data,
        'form': form,
        'comments': comments,
    }
    return render(request, 'blog/detailview.html', context)