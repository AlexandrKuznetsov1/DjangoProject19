from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


# Create your views here.
def myblog(request):
    post = Post.objects.all()  # order_by - сортировка, ('-created_at') - дата создания
    paginate_blog = request.GET.get('paginate_blog', 1) or 1
    paginator = Paginator(post, paginate_blog)  #  пагинируем post по 2 на странице
    page_number = request.GET.get('page')  # из request получаем текущую страницу на которой пользователь
    page_obj = paginator.get_page(page_number)  # формируем объект страницы
    return render(request, 'myblog.html', {'page_obj': page_obj, 'paginate_blog': paginate_blog})  # возвращаем всё пользователю