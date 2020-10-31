from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from timer_app.forms.subtopic import SubTopicForm
from timer_app.models import Topic, SubTopic


def get_topic_choices(request):
    topics = Topic.objects.filter(user=request.user)
    return [(topic.id, topic.name) for topic in topics]


def create_subtopic_form_with_topic_choices(request, subtopic):
    topic_choices = get_topic_choices(request)
    form = SubTopicForm(instance=subtopic)
    form.fields['topic'].choices = [(0, 'Select topic')] + topic_choices
    form.base_fields['topic'].choices = [(0, 'Select topic')] + topic_choices
    return form


@login_required
def create_and_list_subtopic(request):
    if request.method == 'GET':
        context = {
            'form': create_subtopic_form_with_topic_choices(request, SubTopic()),
            'subtopics': SubTopic.objects.filter(user=request.user).order_by('name')
        }

        if not get_topic_choices(request):
            context['error'] = 'Please, first create a topic. Subtopic should have a topic'
        return render(request, 'timer/subtopic_create_and_list.html', context)

    elif request.method == 'POST':
        form = SubTopicForm(request.POST)
        context = {
            'form': form,
        }

        if form.is_valid():
            topic_id = int(form.cleaned_data['topic'])

            try:
                current_topic = Topic.objects.get(pk=topic_id)

                subtopic = SubTopic(name=form.cleaned_data['name'], topic=current_topic)
                subtopic.user = request.user
                subtopic.save()

                current_topic.subtopic_set.add(subtopic)
                current_topic.save()
                return redirect('create_and_list_subtopic')

            except Topic.DoesNotExist:
                context['error'] = 'Topic does not exist. Please, select a topic'
                return render(request, 'timer/subtopic_create_and_list.html', context)

        return render(request, 'timer/subtopic_create_and_list.html', context)


@login_required
def edit_subtopic(request, subtopic_id: int):
    subtopic = SubTopic.objects.get(pk=subtopic_id)

    if request.method == 'GET':
        form = create_subtopic_form_with_topic_choices(request, subtopic)
        form.fields['topic'].initial = subtopic.topic.id

        return render(request, 'timer/subtopic_edit.html', {'form': form})

    elif request.method == 'POST':
        form = SubTopicForm(request.POST, instance=subtopic)

        if not form.is_valid():
            return render(request, 'timer/subtopic_edit.html', {'form': form})

        subtopic = form.save(commit=False)
        subtopic.user = request.user
        subtopic.save()
        return redirect('create_and_list_subtopic')


@login_required
def delete_subtopic(request, subtopic_id: int):
    pass