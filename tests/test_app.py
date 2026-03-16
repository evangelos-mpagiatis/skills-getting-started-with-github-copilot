
import pytest
from backend_pom.actions import get_activities, signup_for_activity, unregister_participant
from backend_pom.assertions import (
    assert_get_activities_success,
    assert_signup_success,
    assert_signup_already_exists,
    assert_unregistration_success,
    assert_not_found
)

def test_get_activities():
    response = get_activities()
    assert_get_activities_success(response)

def test_signup_success():
    activity = "Chess Club"
    email = "newstudent@mergington.edu"
    response = signup_for_activity(activity, email)
    assert_signup_success(response, activity, email)
    # Clean up
    unregister_participant(activity, email)

def test_signup_already_exists():
    activity = "Chess Club"
    email = "michael@mergington.edu"
    response = signup_for_activity(activity, email)
    assert_signup_already_exists(response)

def test_unregistration_success():
    activity = "Programming Class"
    email = "tempuser@mergington.edu"
    signup_for_activity(activity, email)
    response = unregister_participant(activity, email)
    assert_unregistration_success(response, activity, email)

def test_unregistration_not_found():
    activity = "Programming Class"
    email = "notfound@mergington.edu"
    response = unregister_participant(activity, email)
    assert_not_found(response)
