from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import FormView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Unite
from .forms import PreinscriptionForm, FichgramForms


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


class FichegramView(LoginRequiredMixin, UpdateView):
    template_name = 'tangram/fichgram.html'
    success_url = '/fichgrams/'

    def dispatch(self, request, *args, **kwargs):
        if not Unite.objects.filter(user=request.user).exists():
            return redirect('/respos/inscription/')
        return super(FichegramView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(Unite, user=self.request.user)

    def get_form_class(self):
        numero = int(self.kwargs.get('numero'))
        return(FichgramForms[numero - 1])


fichgram = FichegramView.as_view()
