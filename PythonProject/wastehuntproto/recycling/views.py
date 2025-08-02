from django.shortcuts import render

from .forms import GarbageForm
from .models import Garbage

# Define your point and type dictionaries
point_dict = {"plasticbottle": 5, "can": 10}
type_dict = {"plasticbottle": "plastic", "can": "metal"}

def recycle_view(request):
    if request.method == 'POST':
        form = GarbageForm(request.POST)
        if form.is_valid():
            garbage_name = form.cleaned_data['garbage']
            type2 = type_dict[garbage_name]
            point2 = point_dict[garbage_name]

            # Create an instance of Garbage
            garbage_instance = Garbage(name=garbage_name, type=type2, recycled_point=point2)
            info = garbage_instance.display_information()
            recycle_message = garbage_instance.recycle()

            return render(request, 'recycling/result.html', {'info': info, 'recycle_message': recycle_message})
    else:
        form = GarbageForm()

    return render(request, 'recycling/recycle.html', {'form': form})

