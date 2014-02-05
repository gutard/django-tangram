from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import FormView, UpdateView, TemplateView, ListView, CreateView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

from .models import Unite, FicheAction
from .forms import PreinscriptionForm, FichgramForms, FicheActionForm


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
        url = self.request.GET.get('next')
        if url:
            return redirect(url)
        return super(InscriptionView, self).form_valid(form)

inscription = InscriptionView.as_view()


class FichegramView(UpdateView):
    template_name = 'tangram/fichgram.html'
    success_url = '/fichgrams/'

    @method_decorator(login_required)
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


class FichegramsView(TemplateView):
    template_name = 'tangram/fichgrams.html'

    def get_context_data(self, **kwargs):
        context = super(FichegramsView, self).get_context_data(**kwargs)
        try:
            context['unite'] = Unite.objects.get(user=self.request.user)
        except:
            context['unite'] = None
        return context

fichgrams = FichegramsView.as_view()


class GramsView(TemplateView):
    template_name = 'tangram/grams.html'

    def get_context_data(self, **kwargs):
        context = super(GramsView, self).get_context_data(**kwargs)
        unites = Unite.objects.order_by('-nb_grams', 'branche', 'nom')
        context['unites'] = unites
        return context

grams = GramsView.as_view()


class FicheListView(ListView):
    model = FicheAction

fiches = FicheListView.as_view()


class FicheDetailView(DetailView):
    model = FicheAction

fiche = FicheDetailView.as_view()


class FicheFormMixin(object):
    model = FicheAction
    form_class = FicheActionForm
    success_url = reverse_lazy('fiches')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class CreateFicheView(FicheFormMixin, CreateView):
    pass

ajouter_fiche = CreateFicheView.as_view()


class UpdateFicheView(FicheFormMixin, UpdateView):
    pass

modifier_fiche = UpdateFicheView.as_view()
