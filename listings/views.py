from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices

from .models import Listing
from spam.models import Spam_filtering


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings,
                          6)  # listing the houses no. i.e kati wota house dhekhaune 1 page ma .that we want can be changes by change the interger value 3
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings

    }

    return render(request, 'listings/listings.html', context)

@login_required(login_url="/accounts/login")
def listing(request,listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    comments = Spam_filtering.objects.filter(listing=listing, type='ham').order_by('-id')

    context = {
        'listing': listing,
        'comments': comments,
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    #keywords
    if 'keywords' in request.GET:
      keywords =request.GET['keywords']
      if keywords:
          queryset_list = queryset_list.filter(description__icontains=keywords)
    
    # City
    if 'city' in request.GET:
      city =request.GET['city']
      if city:
          queryset_list = queryset_list.filter(city__iexact=city)


    
    # Bedrooms
    if 'price' in request.GET:
      price =request.GET['price']
      if price:
          queryset_list = queryset_list.filter(price__lte=price)

     # Price
    if 'bedrooms' in request.GET:
      bedrooms =request.GET['bedrooms']
      if bedrooms:
          queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    context = {
          
          'bedroom_choices':bedroom_choices,
          'price_choices':price_choices,
          'listings': queryset_list,
          'values': request.GET
    }

    return render(request, 'listings/search.html', context)


'''
Listing template
<!--  <div class="modal fade" id="inquiryModal" role="dialog">-->
<!--    <div class="modal-dialog">-->
<!--      <div class="modal-content">-->
<!--        <div class="modal-header">-->
<!--          <h5 class="modal-title" id="inquiryModalLabel">Make An Inquiry</h5>-->
<!--          <button type="button" class="close" data-dismiss="modal">-->
<!--            <span>&times;</span>-->
<!--          </button>-->
<!--        </div>-->
<!--        <div class="modal-body">-->
<!--          <form action="{% url 'contact' %}" method="POST">-->
<!--            {% csrf_token %}-->
<!--            {% if user.is_authenticated %}-->
<!--              <input type="hidden" name="user_id" value="{{ user.id }}">-->
<!--            {% else %}-->
<!--              <input type="hidden" name="user_id" value="0">             -->
<!--            {% endif %}-->
<!--            <input type="hidden" name="realtor_email" value="{{ listing.realtor.email }}">-->
<!--            <input type="hidden" name="listing_id" value="{{ listing.id }}">-->
<!--            <div class="form-group">-->
<!--              <label for="property_name" class="col-form-label">Property:</label>-->
<!--              <input type="text" name="listing" class="form-control" value="{{ listing.title }}">-->
<!--            </div>-->
<!--            <div class="form-group">-->
<!--              <label for="name" class="col-form-label">Name:</label>-->
<!--              <input type="text" name="name" class="form-control" {% if user.is_authenticated %} value="{{ user.first_name }} {{ user.last_name }}"{% endif %} required>-->
<!--            </div>-->
<!--            <div class="form-group">-->
<!--              <label for="email" class="col-form-label">Email:</label>-->
<!--              <input type="email" name="email" class="form-control" {% if user.is_authenticated %} value="{{ user.email }}"{% endif %}required>-->
<!--            </div>-->
<!--            <div class="form-group">-->
<!--              <label for="phone" class="col-form-label">Phone:</label>-->
<!--              <input type="text" name="phone" class="form-control">-->
<!--            </div>-->
<!--            <div class="form-group">-->
<!--              <label for="message" class="col-form-label">Message:</label>-->
<!--              <textarea name="message" class="form-control"></textarea>-->
<!--            </div>-->
<!--            <hr>-->
<!--            <input type="submit" value="Send" class="btn btn-block btn-secondary">-->
<!--          </form>-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->
'''