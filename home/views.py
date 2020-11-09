from django.shortcuts import render,HttpResponse, get_object_or_404, HttpResponseRedirect
from .models import *
from django.template import loader
from django.contrib.auth import get_user
# Create your views here.


def cat_name(cname):                    # returns Category name
    return cat.get(category_name=cname)


all_photos = Photo.objects.all()            # gets all photos from Photo table
cat = Categories.objects.all()              # gets all photos from Category table
trending_pics = all_photos[5:10]            # select photo of id from 5 to 10


# Logic for rendering Home Page
def home(request):
    # Getting Some photos of popular category
    city_pic = Photo.objects.filter(category=cat.get(category_name='Digital'))[:5]
    nature_pic = Photo.objects.filter(category=cat.get(category_name='Painting'))[:5]
    brand_pic = Photo.objects.filter(category=cat.get(category_name='Photography'))[:5]
    devotion_pic = Photo.objects.filter(category=cat.get(category_name='Graffiti'))[:5]
    back_pic = Photo.objects.filter(category=cat.get(category_name='Background'))[:5]
    mountain_pic = Photo.objects.filter(category=cat.get(category_name='Mountains'))[:5]
    animal_pic = Photo.objects.filter(category=cat.get(category_name='Animals'))[:5]
    # Setting up context which will be used in template for data binding
    context = {
        'all_photos': all_photos,
        'cat': cat,
        'city_pic': city_pic,
        'brand_pic': brand_pic,
        'nature_pic': nature_pic,
        'devotion_pic': devotion_pic,
        'back_pic': back_pic,
        'mountain_pic': mountain_pic,
        'animal_pic': animal_pic,
        'cat_name_city': cat_name('City'),
        'cat_name_nature': cat_name('Nature'),
        'cat_name_animal': cat_name('Animals'),
        'cat_name_mountain': cat_name('Mountains'),
        'cat_name_brand': cat_name('Brand Logo'),
        'cat_name_devotion': cat_name('Devotional'),
        'cat_name_digital': cat_name('Digital'),
        'cat_name_painting': cat_name('Painting'),
        'cat_name_photography': cat_name('Photography'),
        'cat_name_graffiti': cat_name('Graffiti'),

        'trending_pics': trending_pics
    }
    template = loader.get_template('home.html')         # Getting Template
    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))


# Logic for rendering details Page
def details(request, photo_id):
    context = {}
    template = loader.get_template('details.html')          # Getting Template
    photo = get_object_or_404(Photo, pk=photo_id)
    tag_list = photo.tags.split()
    context['tag_list'] = tag_list
    context['photo_id'] = photo_id
    context['photo'] = photo
    context['button_text'] = 'Add to Collection'
    if request.user.is_authenticated:
        order_exist = Order.objects.filter(user=request.user, photo=photo_id)
        context['order_exist'] = order_exist
        collected_pic = Coll.objects.filter(user=request.user, photo=photo_id)
        if request.method == 'POST':
            print('First Checkpoint...')
            if not collected_pic:
                p = Photo.objects.get(id=photo_id)
                c = Coll(user=request.user, photo=p)
                c.save()
                context['button_text'] = 'Remove From Collection'
                return HttpResponse(template.render(context, request))
            else:
                p = Photo.objects.get(id=photo_id)
                Coll.objects.filter(user=request.user, photo=p).delete()
                context['button_text'] = 'Add to Collection'
                return HttpResponse(template.render(context, request))
        context['button_text'] = 'Add to Collection'
        if collected_pic:
            context['button_text'] = 'Remove From Collection'
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))


# Logic for rendering Category Page
def categories(request, cat_id):
    context = {}
    cat_obj = get_object_or_404(Categories, pk=cat_id)
    cat_pics = Photo.objects.filter(category=cat_id)
    template = loader.get_template('category.html')
    context['cat'] = cat
    context['catObject'] = cat_obj
    context['catPics'] = cat_pics
    return HttpResponse(template.render(context, request))


# Logic for rendering Collection Page
def collection(request):
    context = {}
    template = loader.get_template('collection.html')
    if request.user.is_authenticated:
        coll = Coll.objects.filter(user=request.user)
        # col_pic = Photo.objects.filter(id=coll.user)
        ids = Coll.objects.values_list('photo', flat=True).filter(user=request.user)
        col_pic = Photo.objects.filter(id__in=set(ids))

        context['col_pic'] = col_pic
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))


# Logic for rendering Photographer Page
def photographer(request):
    context = {}
    author = Photographer.objects.all()
    context['author'] = author
    template = loader.get_template('photographer.html')
    return HttpResponse(template.render(context, request))


# Logic for rendering Photographer details Page
def photographer_details(request, photographer_id):
    context = {}
    template = loader.get_template('photographerdetails.html')
    photographer_object = get_object_or_404(Photographer, pk=photographer_id)
    pics_by = all_photos.filter(photographer=photographer_id)
    context['photographer_object'] = photographer_object
    context['pics_by'] = pics_by
    return HttpResponse(template.render(context, request))


# Logic for rendering invoice Page
def invoice(request):
    template = loader.get_template('invoice.html')
    if request.method == "POST":
        photo_id = request.POST.get("photo_id", "Undefined")
        photo_obj = Photo.objects.get(id=photo_id)
        name = request.POST.get("title", "Undefined")       # Getting Data from form where name="title"
        price = request.POST.get("price", "Undefined")      # Getting Data from form where name="price"
        taxes = "0"
        total_amount = int(price) + int(taxes)
        image_url = request.POST.get("image_url", "Image not found")
        card_number = request.POST.get("card_number", "Undefined")
        order = Order(user=request.user, photo=photo_obj)
        order.save()
        print(get_user(request))
        print(order, " ordered Successfully")
        data = {"name": name,
                "price": price,
                "card_number": card_number,
                "taxes": taxes,
                "total_amount": total_amount,
                "image_url": image_url,
                "order": order.id
                }

        return HttpResponse(template.render(data, request))
    return HttpResponseRedirect('/')
