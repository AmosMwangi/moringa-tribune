from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Article
from .forms import NewsLetterForm

# display home view
def news_of_day(request):
    date = dt.date.today()
    news = Article.todays_news()
    # return render(request, 'all-news/today-news.html', {"date": date,"news":news})
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = NewsLetterForm()
    return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterForm":form})

# display news details
def detail(request,pkid):
    try:
        news=Article.objects.get(id=pkid)
    except DoesNotExist:
        raise Http404()

    return render(request, 'all-news/details.html', {"news":news})

# display old news
def past_days_news(request,past_date):
    try:
        # converts data from the string url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    
    except ValueError:
        # raise 404 error when velue error is thrown
        raise Http404()
        assert False
    
    if date == dt.date.today():
        return redirect(news_Today)

    news = Article.days_news(date) 
    return render(request, 'all-news/past-news.html', {"date": date,"news":news})

# search for news articles by title
def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html', {"message":message, "articles": searched_articles} )
    
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

# single news
def news(request, news_id):
    try:
        news = Article.objects.get(id = news_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "all-news/news.html", {"news":news})