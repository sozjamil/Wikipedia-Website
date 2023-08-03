from django.shortcuts import render, redirect
from markdown2 import Markdown
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = util.get_entry(title.strip())
    markdowner = Markdown()
    if content == None:
        return render(request, 'encyclopedia/error.html', {"message": "Page not found"})
    else:
        return render(request, 'encyclopedia/entry.html', {
            'title': title,
            'content': markdowner.convert(content)
        })


def search(request):
    q = request.GET.get('q', '')
    if (util.get_entry(q) is not None):
        return redirect('wiki:entry', title=q)
    else:
        entries = []
        for entry in util.list_entries():
            if q.lower() in entry.lower():
                entries.append(entry)
        return render(request, "encyclopedia/index.html", {"entries": entries})    


def new(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        markdowner = Markdown()
        if title == "" or content == "":
            return render(request, "encyclopedia/error.html", {"message": "Can't save Page with empty field."})
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/error.html", {"message": "Entry page already exists"})
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": markdowner.convert(content)
        })


def edit(request, title):
    content = util.get_entry(title.strip())
    if request.method == "POST":
        content = request.POST.get("content").strip()
        if content == "":
            return render(request, "encyclopedia/edit.html", {"message": "Can't save with empty field.", "title": title, "content": content})
        util.save_entry(title, content)
        return redirect("wiki:entry", title=title)
    return render(request, "encyclopedia/edit.html", {
        'content': content,
        'title': title
    })


def random_page(request):
    entry_list = util.list_entries()
    entrytitle = random.choice(entry_list)
    markdowner = Markdown()
    content = util.get_entry(entrytitle)
    return render(request, "encyclopedia/entry.html", {
        "title": entrytitle,
        "content": markdowner.convert(content)
    })
