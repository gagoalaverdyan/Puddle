from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EditItemForm, NewItemForm
from .models import Category, Item


def browse(request):
    query = request.GET.get("query", "")
    current_cat_id = int(request.GET.get("category", 0))
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    if current_cat_id:
        items = items.filter(category_id=current_cat_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(
        request,
        "item/browse.html",
        {"items": items, "query": query, "categories": categories, "current_cat_id": current_cat_id},
    )


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:5]
    return render(request, "item/detail.html", {"item": item, "related_items": related_items})


@login_required
def new_item(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect("item:detail", pk=item.id)
    else:
        form = NewItemForm()
    return render(request, "item/form.html", {"form": form, "title": "New item"})


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect("dashboard:index")


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("item:detail", pk=item.id)  # type: ignore
    else:
        form = EditItemForm(instance=item)
    return render(request, "item/form.html", {"form": form, "title": "Edit item"})
