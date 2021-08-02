from django.shortcuts import render

posts = [
    {
        'author' : 'Preeti',
        'date_publish' : 'August 2 2021',
        'title' : 'Preeti BHUT PAGAL H',
        'content' : 'Sahi baat h',
    },
    {
        'author' : 'Priyanshu',
        'date_publish' : 'August 2 2021',
        'title' : 'Preeti PAGAL H',
        'content' : 'Sahi baat h',
    },
    {
        'author' : 'Raghu',
        'date_publish' : 'August 2 2021',
        'title' : 'Preeti PAGAL H',
        'content' : 'Sahi baat h',
    },
]
def home(request):
    context = {
        'posts' : posts,
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')