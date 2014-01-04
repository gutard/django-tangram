from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Unite
from .forms import PreinscriptionForm


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class InscriptionView(LoginRequiredMixin, FormView):
    template_name = 'tangram/inscription.html'
    form_class = PreinscriptionForm
    success_url = '/respos/'

    def get_form_kwargs(self):
        kwargs = super(InscriptionView, self).get_form_kwargs()
        try:
            kwargs['instance'] = Unite.objects.get(user=self.request.user)
        except Unite.DoesNotExist:
            pass
        return kwargs

    def form_valid(self, form):
        unite = form.save(commit=False)
        if not form.instance.pk:
            unite.user = self.request.user
        unite.save()
        return super(InscriptionView, self).form_valid(form)

inscription = InscriptionView.as_view()
