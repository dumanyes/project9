from django.shortcuts import render
from .models import Post

from django.shortcuts import render
from .models import Post

# def index(request):
#     featured_posts = Post.objects.filter(categories__name='featured')[:1]
#     politics_posts = Post.objects.filter(categories__name='politics')[:2]
#     business_posts = Post.objects.filter(categories__name='business_economy')[:2]
#     culture_posts = Post.objects.filter(categories__name='culture')[:2]
#     technology_posts = Post.objects.filter(categories__name='technology')[:2]
#     sports_posts = Post.objects.filter(categories__name='sports')[:2]
#     education_posts = Post.objects.filter(categories__name='education')[:2]
#     environment_posts = Post.objects.filter(categories__name='environment')[:2]
#     travel_posts = Post.objects.filter(categories__name='travel_tourism')[:2]
#     local_news_posts = Post.objects.filter(categories__name='local_news')[:2]
#     international_news_posts = Post.objects.filter(categories__name='international_news')[:2]
#
#     context = {
#         'featured_posts': featured_posts,
#         'politics_posts': politics_posts,
#         'business_posts': business_posts,
#         'culture_posts': culture_posts,
#         'technology_posts': technology_posts,
#         'sports_posts': sports_posts,
#         'education_posts': education_posts,
#         'environment_posts': environment_posts,
#         'travel_posts': travel_posts,
#         'local_news_posts': local_news_posts,
#         'international_news_posts': international_news_posts,
#     }
#     return render(request, 'core/index.html', context)
from django.core.paginator import Paginator
def index(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'core/index.html', context)

def sort_newest(request):
    all_posts = Post.objects.order_by('-created')
    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'core/index.html', context)

def sort_oldest(request):
    all_posts = Post.objects.order_by('created')
    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'core/index.html', context)




def post_detail(request, pk):
    post_detail = Post.objects.get(pk=pk)
    context = {'post_detail': post_detail}
    return render(request, 'core/post_detail.html', context)

from django.shortcuts import render

def politics(request):
    # Query the database for posts categorized as 'politics'
    politics_posts = Post.objects.filter(categories__name='politics')

    # Pass the politics posts to the template for rendering
    return render(request, 'core/politics.html', {'politics_posts': politics_posts})

def business(request):
    # Query the database for posts categorized as 'business and economy'
    business_posts = Post.objects.filter(categories__name='business_economy')

    # Pass the business posts to the template for rendering
    return render(request, 'core/business.html', {'business_posts': business_posts})

def culture(request):
    # Query the database for posts categorized as 'culture'
    culture_posts = Post.objects.filter(categories__name='culture')

    # Pass the culture posts to the template for rendering
    return render(request, 'core/culture.html', {'culture_posts': culture_posts})

def technology(request):
    # Query the database for posts categorized as 'technology'
    technology_posts = Post.objects.filter(categories__name='technology')

    # Pass the technology posts to the template for rendering
    return render(request, 'core/technology.html', {'technology_posts': technology_posts})

def sports(request):
    # Query the database for posts categorized as 'sports'
    sports_posts = Post.objects.filter(categories__name='sports')

    # Pass the sports posts to the template for rendering
    return render(request, 'core/sports.html', {'sports_posts': sports_posts})

def environment(request):
    # Query the database for posts categorized as 'environment'
    environment_posts = Post.objects.filter(categories__name='environment')

    # Pass the environment posts to the template for rendering
    return render(request, 'core/environment.html', {'environment_posts': environment_posts})

def travel(request):
    # Query the database for posts categorized as 'travel and tourism'
    travel_posts = Post.objects.filter(categories__name='travel_tourism')

    # Pass the travel posts to the template for rendering
    return render(request, 'core/travel.html', {'travel_posts': travel_posts})

def local_news(request):
    # Query the database for posts categorized as 'local news'
    local_news_posts = Post.objects.filter(categories__name='local_news')

    # Pass the local news posts to the template for rendering
    return render(request, 'core/local_news.html', {'local_news_posts': local_news_posts})

def international_news(request):
    # Query the database for posts categorized as 'international news'
    international_news_posts = Post.objects.filter(categories__name='international_news')

    # Pass the international news posts to the template for rendering
    return render(request, 'core/international_news.html', {'international_news_posts': international_news_posts})

def education_news(request):
    # Query the database for posts categorized as 'education'
    education_news_posts = Post.objects.filter(categories__name='education')

    # Pass the education news posts to the template for rendering
    return render(request, 'core/education_news.html', {'education_news_posts': education_news_posts})

from django.db.models import Q


def search_results(request):
    query = request.GET.get('q')
    order = request.GET.get('order', 'desc')

    if query:
        search_results = Post.objects.filter(title__icontains=query)
        if order == 'asc':
            search_results = search_results.order_by('created')
        else:
            search_results = search_results.order_by('-created')
    else:
        search_results = []

    context = {
        'search_results': search_results,
        'order': order
    }
    return render(request, 'core/search_results.html', context)