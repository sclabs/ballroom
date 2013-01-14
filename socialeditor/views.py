from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from models import Profile, Routine, Video

def home(request):
    # list profiles tied to user if logged in
    return HttpResponse("Hello, world!")

def create_profile(request):
    return  HttpResponse("Creating profile on user " + request.user.username)

def view_profile(request, short_name):
    profile = get_object_or_404(Profile, short_name=short_name)
    # list routines tied to this profile
    return HttpResponse("Viewing profile of " + profile.display_name)

def add_friend(request, short_name, add_short_name):
    profile = get_object_or_404(Profile, short_name=short_name)
    # make sure the current user owns the profile, if not error
    friend = get_object_or_404(Profile, short_name=add_short_name)
    return HttpResponse("Adding friend " + friend.display_name)

def remove_friend(request, short_name, remove_short_name):
    profile = get_object_or_404(Profile, short_name=short_name)
    # make sure the current user owns the profile, if not error
    friend = get_object_or_404(Profile, short_name=remove_short_name)
    return HttpResponse("Removing friend " + friend.display_name)

def delete_profile(request, short_name):
    profile = get_object_or_404(Profile, short_name=short_name)
    # make sure the current user owns the profile, if not error
    return HttpResponse("Deleting profile " + profile.display_name)

def create_routine(request, short_name):
    profile = get_object_or_404(Profile, short_name=short_name)
    # do the usual if request.method == 'POST': split
    # the url should be in request.POST['url'], etc
    # make sure the current user owns the profile, if not error
    return  HttpResponse("Creating routine on profile " + profile.display_name)

def view_routine(request, short_name, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)
    profile = get_object_or_404(Profile, short_name=short_name)
    # check if the profile owns the routine, if not 404
    return HttpResponse("Viewing routine " + routine.title)

def edit_routine(request, short_name, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)
    profile = get_object_or_404(Profile, short_name=short_name)
    # check if the profile owns or is an editor on the routine, if not 404
    # make sure the current user owns the profile, if not error
    return HttpResponse("Editing routine " + routine.title)

def save_routine(request, short_name, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)
    profile = get_object_or_404(Profile, short_name=short_name)
    # check if the profile owns the routine, if not 404
    # make sure the current user owns the profile, if not error
    # write the timeline into the database
    return HttpResponse("Saving routine " + routine.title)

def add_video(request, short_name, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)
    profile = get_object_or_404(Profile, short_name=short_name)
    # check if the profile owns the routine, if not 404
    # make sure the current user owns the profile, if not error
    # do the usual if request.method == 'POST': split
    # the url should be in request.POST['url'], etc
    return HttpResponse("Adding video to " + routine.title)

def edit_video(request, short_name, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)
    profile = get_object_or_404(Profile, short_name=short_name)
    video = get_object_or_404(Video, id=video_id)
    # check if the profile owns the routine, if not 404
    # make sure the current user owns the profile, if not error
    # check if the video foreignkeys into the routine, if not 404
    # do the usual if request.method == 'POST': split
    # the url should be in request.POST['url'], etc
    return HttpResponse("Editing video " + video.title)

def remove_video(request, short_name, routine_id, video_id):
    routine = get_object_or_404(Routine, id=routine_id)
    profile = get_object_or_404(Profile, short_name=short_name)
    video = get_object_or_404(Video, id=video_id)
    # check if the profile owns the routine, if not 404
    # check if the video foreignkeys into the routine, if not 404
    # make sure the current user owns the profile, if not, error
    return HttpResponse("Removing video " + video.title)

def delete_routine(request, short_name, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)
    profile = get_object_or_404(Profile, short_name=short_name)
    # check if the profile owns the routine, if not 404
    # make sure the current user owns the profile, if not, error
    return HttpResponse("Deleting routine " + routine.title)
