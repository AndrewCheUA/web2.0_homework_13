from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from .forms import TagForm, QuoteForm, AuthorForm
from .models import Tag, Quote, Author


# Create your views here.
def main(request):
    quotes = Quote.objects.filter().all()
    return render(request, 'quoteapp/index.html', {"quotes": quotes})


def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/tag.html', {'form': form})

    return render(request, 'quoteapp/tag.html', {'form': TagForm()})


def quote(request):
    tags = Quote.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_note = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_note.tags.add(tag)

            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/quote.html', {"tags": tags, 'form': form})

    return render(request, 'quoteapp/quote.html', {"tags": tags, 'form': QuoteForm()})


@login_required()
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/authoradd.html', {'form': form})

    return render(request, 'quoteapp/authoradd.html', {'form': AuthorForm()})


def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quoteapp/detail.html', {"quote": quote})


@login_required
def delete_quote(request, quote_id):
    Quote.objects.get(pk=quote_id).delete()
    return redirect(to='quoteapp:main')


def author_page(request, fullname):
    authors = get_object_or_404(Author, fullname=fullname)

    return render(request, "quoteapp/author.html", {"author": authors})
