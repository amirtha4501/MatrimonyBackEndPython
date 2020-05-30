from controller import check, register, list_profiles, view_profile

ROUTES = [

    ('GET', '/', check),

    ('POST', '/register', register),

    ('GET', '/profiles', list_profiles),

    ('GET', '/profiles/<int:profile_id>', view_profile)
]