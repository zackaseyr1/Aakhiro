# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Listing
from .forms import ListingForm

def listing_list(request):
    listings = Listing.objects.filter(published=True)
    return render(request, 'listing_list.html', {'listings': listings})

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'listing_detail.html', {'listing': listing})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listing-list')
    else:
        form = ListingForm()
    return render(request, 'listing_form.html', {'form': form})

def listing_update(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing-list')
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listing_form.html', {'form': form})

def listing_delete(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if request.method == 'POST':
        listing.delete()
        return redirect('listing-list')
    return render(request, 'listing_confirm_delete.html', {'listing': listing})
