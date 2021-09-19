from django.core import paginator
from django.db.models.base import Model
from django.forms.models import construct_instance
from django.shortcuts import render,get_object_or_404 ,redirect ,HttpResponseRedirect
from django.contrib import messages
from .models import Category, Comment, Note, PostModel
from .forms import CommentForm , searchForm
from django.views.generic import DetailView,ListView
from django.template import RequestContext
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.postgres.search import SearchVector, SearchQuery,SearchRank

"""def index(request):
	messages.add_message(request, messages.INFO, 'Hello world.')
	return render(request,'index.html')"""
class index(ListView):
	model= PostModel
	template_name="index.html"
	paginate_by = 3


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		nots = Note.objects.filter(status = 's').all()
		nots_count = Note.objects.filter(status = 's').all().count()
		context['nots_list'] = nots
		context['count']= (1,nots_count+1)
		return context

	
def single (request,slug):

	
	object=get_object_or_404(PostModel, slug=slug , status = 'p')
	ip_address = request.user.ip_address
		# if user.is_autenticated and ...
	if ip_address not in object.views.all():
		object.views.add(ip_address)
	new_comment = None
	#comments = Comment.objects.filter(post = object , status = True)
	comments = object.comments.filter(status = True)
	#get similar post
	similar_posts= PostModel.objects.filter(category = object.category).exclude(id=object.id).\
		order_by('publish')[:2]

	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			reply_obj = None
			# get parent comment id from hidden input
			try:
				# id integer e.g. 15
				reply_id = int(request.POST.get('reply_id'))
			except:
				reply_id = None
			if reply_id :
				reply_obj = Comment.objects.get (id = reply_id)
				if reply_obj :
					# create replay comment object
					replay_comment = comment_form.save(commit=False)
					# assign parent_obj to replay comment
					replay_comment.reply = reply_obj

			# Create Comment object but don't save to database yet
			new_comment = comment_form.save(commit=False)
			# Assign the current post to the comment
			new_comment.post = object
			# Save the comment to the database
			new_comment.save()

			return HttpResponseRedirect(object.get_absolute_url())
			
	else:
		comment_form = CommentForm()
	return render(request,'single.html', {'object': object,
										   'comments': comments,
											'new_comment' : new_comment,
										   'comment_form': comment_form,
										   'similars':similar_posts,
										   })

def listofcategory(request,slug):
	cat_slug = Category.objects.get(slug=slug)
	posts= PostModel.objects.filter(category =cat_slug).order_by('-publish')
	paginator = Paginator(posts,3)
	page = request.GET.get('page',1)
	try:
		postes = paginator.page(page)
	except PageNotAnInteger:
		postes = paginator.page(1)
	except EmptyPage:
		postes= paginator.page(paginator.num_pages)
	contex = {
		'object_list':postes
	}
	return render(request,"list.html",context=contex)

def searchView(request):
	result = []
	query =""
	form = searchForm()
	if 'query' in request.GET:

		
		
			query = request.GET.get('query')
			search_vector = SearchVector('title',weight='A')+SearchVector('body',weight = 'B')
			search_query = SearchQuery(query)
			result =PostModel.objects.filter(status= 'p')
			result = result.annotate(
				rank= SearchRank(search_vector,search_query)

			).filter(rank__gte=0.3).order_by('-rank')

	return render (request,'search.html',{'results':result, 'query':query})

def about(request):
	return render(request,'about.html')



		


