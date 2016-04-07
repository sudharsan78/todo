from django.shortcuts import render
from django.template import loader
from .forms import WrkForm
from django.http import HttpResponse
from .models import Wrk

def index(request):
    wrk_info=Wrk.objects.all()
    #template=loader.get_template('tdlist/index.html')
    context={'wrk_info':wrk_info,}

    #return HttpResponse(template.render(context, request))
    return render(request, 'tdlist/index.html', context)
    #html="<html><body>fghdfh%s</body></html>"
    #return HttpResponse(html)
    #return HttpResponse("todolist under construction")
    #latest_wrk_lst=Wrk.object.order_by()
    #output=', '.join([w.wrk_lst for w in latest_wrk_lst ])
    #return Httpresponse(output)

def add_wrk(request):
    context=RequestContext(request)
    if request.method=='POST':
        form=WrkForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render_to_responde('tdlist/index.html',{'form':form}, context)

#def get_wrk(request):
#    if request.method=='POST':
#        form = WrkForm(request.POST)
#        if form.is_valid():
#            if form==Wrk.wrk_lst:
#                return HttpResponse('the work already exist')
#            else :
#                w=Wrk(wrk_lst=form)
#                w.save()

#    return render(request,'index.html', {'form':form})
