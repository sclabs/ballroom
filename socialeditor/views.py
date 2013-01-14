from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from models import Profile, Routine, Video

# home #
########

def home(request):
    return HttpResponse("Hello, world!")

# profiles #
############

def view_profile(request, short_name):
    profile = get_object_or_404(Profile, short_name=short_name)
    return HttpResponse("Viewing profile of " + profile.display_name)

def edit_profile(request, short_name):
    profile = get_object_or_404(Profile, short_name=short_name)
    if request.user.profile != profile:
        # error!
    return HttpResponse("Editing profile of " + profile.display_name)

# friends #
###########

def add_friend(request, short_name):
    friend = get_object_or_404(Profile, short_name=short_name)
    return HttpResponse("Adding friend " + friend.display_name)

def remove_friend(request, short_name):
    friend = get_object_or_404(Profile, short_name=short_name)
    return HttpResponse("Removing friend " + friend.display_name)

# groups #
##########

def create_group(request):
    # do the usual if request.method == 'POST': split
    return  HttpResponse("Creating group")

def view_group(request, short_name):
    group = get_object_or_404(Group, short_name=short_name)
    return HttpResponse("Viewing group " + group.display_name)

def edit_group(request, short_name):
    group = get_object_or_404(Group, short_name=short_name)
    if request.user.profile not in group.members:
        # error!
    # do the usual if request.method == 'POST': split
    return HttpResponse("Editing group " + group.display_name)

def add_member(request, group_short_name, member_short_name):
    group = get_object_or_404(Group, short_name=group_short_name)
    member = get_object_or_404(Profile, short_name=member_short_name)
    if request.user.profile not in group.members:
        # error!
    return HttpResponse("Adding to group " + group.display_name)

def leave_group(request, short_name):
    group = get_object_or_404(Group, short_name=short_name)
    if request.user.profile not in group.members:
        # error!
    return HttpResponse("Leaving group " + group.display_name)

# routines #
############

def create_routine(request):
    # do the usual if request.method == 'POST': split
    return  HttpResponse("Creating routine")

def view_routine(request, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)
    return HttpResponse("Viewing routine " + routine.title)

def edit_routine(request, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)
    if not routine_editable(request.user, routine):
        # error!
    return HttpResponse("Editing routine " + routine.title)

def save_routine(request, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)
    if not routine_editable(request.user, routine):
        # error!
    # write the timeline into the database
    return HttpResponse("Saving routine " + routine.title)

def delete_routine(request, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)
    if not routine_editable(request.user, routine):
        # error!
    return HttpResponse("Deleting routine " + routine.title)

# videos #
##########

def add_video(request, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)
    if not routine_editable(request.user, routine):
        # error!
    # do the usual if request.method == 'POST': split
    return HttpResponse("Adding video to " + routine.title)

def edit_video(request, routine_id, video_id):
    routine = get_object_or_404(Routine, id=routine_id)
    video = get_object_or_404(Video, id=video_id)
    if not routine_editable(request.user, routine):
        # error!
    if video.routine != routine:
        # 404!
    # do the usual if request.method == 'POST': split
    return HttpResponse("Editing video " + video.title)

def remove_video(request, routine_id, video_id):
    routine = get_object_or_404(Routine, id=routine_id)
    video = get_object_or_404(Video, id=video_id)
    if not routine_editable(request.user, routine):
        # error!
    if video.routine != routine:
        # 404!
    return HttpResponse("Removing video " + video.title)

# utility methods #
###################

def routine_editable(user, routine):
    # get the user's profile
    profile = user.profile

    # check if edit has been granted explicitly
    if routine in profile.editable_routines:
        return True

    # check if edit is inherited through group membership
    for group in profile.member_of:
        if routine in group.editable_routines:
            return True

    # no hits, return False
    return False
