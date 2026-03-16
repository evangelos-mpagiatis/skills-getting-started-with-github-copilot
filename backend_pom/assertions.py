def assert_get_activities_success(response):
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "Chess Club" in response.json()

def assert_signup_success(response, activity_name, email):
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity_name}"

def assert_signup_already_exists(response):
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]

def assert_unregistration_success(response, activity_name, email):
    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {email} from {activity_name}"

def assert_not_found(response):
    assert response.status_code == 404
