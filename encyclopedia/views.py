from django.shortcuts import render
from markdown2 import Markdown
import random

from . import util

def convert_md(entry_name):
    markdowner = Markdown()
    if util.get_entry(entry_name):
        entry = util.get_entry(entry_name)
        return markdowner.convert(entry)
    return None
      
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def make_entry(request, entry_name):
    if convert_md(entry_name) == None:
        return render(request, "encyclopedia/error.html")
    return render(request, "encyclopedia/entry.html/", {
        "entry_name" : entry_name,
        "entry": convert_md(entry_name)
    })

def search(request):
    if request.method == "POST":
        search_name = request.POST['q']
        # if search_name.isValid():
        if convert_md(search_name) is not None:
            return render(request, "encyclopedia/entry.html/", {
                "entry_name" : search_name,
            "entry": convert_md(search_name)
        }) 
        # find substrings and add to new file
        else:
            sub = []
            for entry in util.list_entries():
                if search_name.lower() in entry.lower():
                    sub.append(entry)
                
            # return error
            if sub:
                return render(request, "encyclopedia/search.html", {
                    "results" : sub
                })
                # print("search else")
    return render(request, "encyclopedia/error.html")

def create(request):
    if request.method == "POST":
        #assigned vars
        entry_name = request.POST['title']
        entry_content = request.POST['content']

        # return error page if title already exists
        if convert_md(entry_name) is not None:
            return render(request, "encyclopedia/create_error.html")
        
        else:
            util.save_entry(entry_name, entry_content)
            return render(request, "encyclopedia/entry.html", {
                    "entry_name" : entry_name,
                    "entry": convert_md(entry_name)
            })
    return render(request, "encyclopedia/create.html")

def random_entry(request):
    rand = random.choice(util.list_entries())
    return render(request, "encyclopedia/entry.html", {
        "entry_name" : rand,
        "entry" : convert_md(rand)
    })

def edit(request, edit_name):
    return render(request, "encyclopedia/edit_page.html", {
        "edit_name": edit_name,
        "curr_content":util.get_entry(edit_name)
    })

def save_edit(request, entry_name):
    if request.method == "POST":
        #assigned vars
        entry_content = request.POST['content']
        print(entry_content)
        edited_entry = util.save_entry(entry_name, entry_content)

        return render(request, "encyclopedia/entry.html", {
            "entry_name":entry_name, 
            "entry":convert_md(entry_name)
        })
    return render(request, "encyclopedia/edit_page.html")




         


 