from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from listings.choices import state_choices, bedroom_choices, price_choices

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
        }
    return render(request, 'listings/listings.html', context )
# def listings(request):
#     return render(request, 'listings/listings.html')

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
       
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    
    context = {
      
         'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'listings/search.html', context)