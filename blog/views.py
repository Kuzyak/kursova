from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from PIL import Image, ImageOps, ImageFilter
from .forms import PostForm
from .models import Post
from .models import Teg

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

def foto_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/foto_view.html', {'post': post})
'''
def foto_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('foto_view', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/foto_edit.html', {'form': form,'post': post})
'''
def applyfilter(pk, preset):
    post = get_object_or_404(Post, pk=pk)
    infile = post.images.url
    f = infile.split('.')
    newfile =  f[0] + '-new.' + f[1]
    f = newfile.split('/')
    newfilename = f[-1]
    infile.replace("/","//")
    im = Image.open(infile)
    if preset == 'gray':
        im = ImageOps.grayscale(im)

    if preset == 'edge':
        im = ImageOps.grayscale(im)
        im = im.filter(ImageFilter.FIND_EDGES)

    if preset == 'poster':
        im = ImageOps.posterize(im,3)

    if preset == 'solar':
        im = ImageOps.solarize(im, threshold=80)

    if preset == 'blur':
        im = im.filter(ImageFilter.BLUR)

    if preset == 'sepia':
        sepia=[]
        #sepia2=[]
        r,g,b=(239,224,185)
        for i in range(255):
            sepia.extend((r*i//255,g*i//255,b*i//255))
        #for i in sepia:
        #    if i>0:
        #        n=i-i%i
        #    else: n=0
        #    sepia2.extend(n)
        #print (sepia2)
        im = im.convert("L")
        im.putpalette(sepia)
        im = im.convert("RGB")

    im.save(newfile)
    return newfilename


def foto_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print (form.errors)
        if form.is_valid():
            preset = request.POST['preset']
            newfilename = applyfilter(pk,preset)
            return render_to_response('blog/foto_out.html', {'newfilename':newfilename}, context_instance = RequestContext(request))
    else:
        form = PostForm(instance=post)
    return render_to_response('blog/foto_edit.html',{'form':form,'post': post},context_instance = RequestContext(request))

def foto_out(request):
    return render_to_response('blog/foto_out.html',{})
