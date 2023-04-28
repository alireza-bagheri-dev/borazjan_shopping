from django.views import generic
from django.shortcuts import get_object_or_404, reverse, render
from django.utils.translation import gettext as _
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .models import Product, Comment
from .forms import CommentForm


class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(active=True).order_by('datetime_created')
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 4

    # def get_queryset(self):
    #

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm

    # def get_success_url(self):
    #     return reverse('product_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product

        messages.success(self.request, _('Comment successfully created'))

        return super().form_valid(form)


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    fields = ['title', 'description', 'short_description', 'price', 'active', 'image',]
    template_name = 'Products/product_create.html'


# class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
#     model = Product
#     fields = ['title', 'description', 'short_description', 'price', 'active', 'image', ]
#     template_name = 'Product/product_update.html'
#
#     def test_func(self):
#         obj = self.get_object()
#         return obj.user == self.request.user

#
# class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
#     model = Product
#     template_name = 'Product/Product_delete.html'
#     success_url = reverse_lazy('product_list')
#
#     def test_func(self):
#         obj = self.get_object()
#         return obj.user == self.request.user