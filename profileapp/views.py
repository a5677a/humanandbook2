
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import pf_ownership_required
from profileapp.forms import ProfileCreation
from profileapp.models import Profile

class PfCreate(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreation
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})


@method_decorator(pf_ownership_required, 'get')
@method_decorator(pf_ownership_required, 'post')
class PfUpdate(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreation
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})