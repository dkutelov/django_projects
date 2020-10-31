from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from timer_app.forms.topic import TopicForm
from timer_app.models import Topic


@login_required
def create_and_list_topic(request):
    topics = Topic.objects.filter(user=request.user)
    context = {
        'form': TopicForm(),
        'topics': topics
    }

    if request.method == 'GET':
        return render(request, 'timer/topic-create-and-list.html', context)

    elif request.method == 'POST':
        form = TopicForm(request.POST)

        if form.is_valid():
            topic = Topic(name=form.cleaned_data['name'])
            topic.user = request.user
            topic.save()
        return render(request, 'timer/topic-create-and-list.html', context)


@login_required
def edit_topic(request, topic_id: int):
    current_topic = Topic.objects.get(pk=topic_id)

    context = {
        'form': TopicForm(instance=current_topic)
    }

    if request.method == 'GET':
        return render(request, 'timer/topic-edit.html', context)

    elif request.method == 'POST':
        form = TopicForm(request.POST, instance=current_topic)

        if not form.is_valid():
            context = {
                'form': form
            }
            return render(request, 'timer/topic-edit.html', context)

        form.save()
        return redirect('create_and_list_topic')


@login_required
def delete_topic(request, topic_id: int):
    topic_to_delete = Topic.objects.get(pk=topic_id)

    if request.method == 'GET':
        return render(request, 'timer/topic-delete.html', {'topic_name': topic_to_delete.name})

    elif request.method == 'POST':
        topic_to_delete.delete()
        return redirect('create_and_list_topic')