from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from items.models import Item
from communicate.models import ConversationU
from .forms import ConversationMessageForm
# Create your views here.
@login_required
def new_conversation(request,item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect ('dashboard:index')
    
    conversation=ConversationU.objects.filter(item=item).filter(members__in=[request.user.id])
    # conversation = ConversationU.objects.filter(item=item, members=request.user)
   


    if conversation:
        
        pass
    if request.method == 'POST':
        form=ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation=ConversationU.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message=form.save(commit=False)
            conversation_message.conversation= conversation
            conversation_message.created_by =request.user
            conversation_message.save()
            return redirect ('items:detail',pk=item_pk)
        
    else:
        form = ConversationMessageForm()

    return render (request,'communicate/new.html',{'forms':form})



@login_required
def inbox(request):

    conversation = ConversationU.objects.filter(members__in=[request.user.id])
    return render(request,'communicate/inbox.html',{'conversation':conversation})

