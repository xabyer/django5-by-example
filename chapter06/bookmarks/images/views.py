from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ImageCreateForm

# Create your views here.
@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data= request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # assing current user to the item
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Image added successfully')
            # redirect to new create item detail view
            return redirect(new_image.get_absolute_url())
    else:
        # build form with data provided by the boorkmarklet via GET
        form = ImageCreateForm(data = request.GET)

    return render(
        request,
        'images/image/create.html',
        {'section': 'images', 'form': form}
    )