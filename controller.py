from flask import request, jsonify, abort
from session import SESSION
from uuid import uuid4

# Check
def check():
    return 'Working'

# Register user
def register():
    input_data = request.get_json()
    from model import Profile

    if Profile.where(email=input_data['email']).first() is not None:
        abort(400, {'message': 'EMAIL_ALREADY_EXISTS'})
    
    profile = Profile.create(
        id = input_data['id'],

        # Personal details
        imageUrls = input_data['imageUrls'],
        name = input_data['name'],
        email = input_data['email'],
        password = input_data['password'],
        gender = input_data['gender'],
        dob = input_data['dob'],
        birth_time = input_data['birth_time'],
        birth_place = input_data['birth_place'],
        religion = input_data['religion'],
        caste = input_data['caste'],
        subcaste = input_data['subcaste'],
        gothram = input_data['gothram'],
        star = input_data['star'],
        qualification = input_data['qualification'],
        job = input_data['job'],
        workplace = input_data['workplace'],
        income = input_data['income'],
        height = input_data['height'],
        weight = input_data['weight'],
        mother_tongue = input_data['mother_tongue'],
        known_language = input_data['known_language'],
        nativity = input_data['nativity'],
        marital_status = input_data['marital_status'],
        talents = input_data['talents'],
        hobbies = input_data['hobbies'],
        vehicle_driving = input_data['vehicle_driving'],
        disabilities = input_data['disabilities'],

        # Horoscope details
        box11 = input_data['box11'],
        box12 = input_data['box12'],
        box13 = input_data['box13'],
        box14 = input_data['box14'],
        box15 = input_data['box15'],
        box16 = input_data['box16'],
        box17 = input_data['box17'],
        box18 = input_data['box18'],
        box19 = input_data['box19'],
        box110 = input_data['box110'],
        box111 = input_data['box111'],
        box112 = input_data['box112'],
        
        box21 = input_data['box21'],
        box22 = input_data['box22'],
        box23 = input_data['box23'],
        box24 = input_data['box24'],
        box25 = input_data['box25'],
        box26 = input_data['box26'],
        box27 = input_data['box27'],
        box28 = input_data['box28'],
        box29 = input_data['box29'],
        box210 = input_data['box210'],
        box211 = input_data['box211'],
        box212 = input_data['box212'],

        # Family details
        father_name = input_data['father_name'],
        father_occupation = input_data['father_occupation'],
        mother_name = input_data['mother_name'],
        mother_occupation = input_data['mother_occupation'],
        contact1 = input_data['contact1'],
        contact2 = input_data['contact2'],
        sibiling_count = input_data['sibiling_count'],
        family_status = input_data['family_status'],
        properties = input_data['properties'],
        anydetails = input_data['anydetails'],

        # Partner Expectations
        expected_qualification = input_data['expected_qualification'],
        expected_place = input_data['expected_place'],
        expected_income = input_data['expected_income'],
        expected_caste = input_data['expected_caste'],
        expected_subcaste = input_data['expected_subcaste'],
        age_difference = input_data['age_difference'],
        expected_height = input_data['expected_height'],
        expected_weight = input_data['expected_weight'],
        expectations = input_data['expectations']
    )

    uuid = str(uuid4())
    SESSION[uuid] = profile
    response_body = {
        'session_id': uuid,
        'id' : profile.id,
        'name': profile.name
    }
    return jsonify(response_body)


# All Profiles Overview
def list_profiles():
    profile = SESSION.get(request.headers.get('Authorization'))
    if profile is None:
        abort(400, {'message': 'TOKEN_NOT_FOUND'})
    from model import Profile
    profile_response = []
    for profile in Profile.query.all():
        profile_response.append({
            'name': profile.name,
            'dob': profile.dob,
            'img': profile.img,
            'star': profile.star,
            'age': profile.age
        })
    return jsonify(profile_response)

# View full profile detail
def view_profile():
    profile = SESSION.get(request.heades.get('Authorization'))
    if profile is None:
        abort(400, {'message': 'TOKEN_NOT_FOUND'})
    from model import Profile
    profile_response = []
    for profile in Profile.query.all():
        profile_response.append({
            'id' : profile.id,

            'imageUrls' : profile.imageUrls,
            'name' : profile.name,
            'email' : profile.email,
            'password' : profile.password,
            'gender' : profile.gender,
            'dob' : profile.dob,
            'birth_time' : profile.birth_time,
            'birth_place' : profile.birth_place,
            'religion' : profile.religion,
            'caste' : profile.caste,
            'subcaste' : profile.subcaste,
            'gothram' : profile.gothram,
            'star' : profile.star,
            'qualification' : profile.qualification,
            'job' : profile.job,
            'workplace' : profile.workplace,
            'income' : profile.income,
            'height' : profile.height,
            'weight' : profile.weight,
            'mother_tongue' : profile.mother_tongue,
            'known_language' : profile.known_language,
            'nativity' : profile.nativity,
            'marital_status' : profile.marital_status,
            'talents' : profile.talents,
            'hobbies' : profile.hobbies,
            'vehicle_driving' : profile.vehicle_driving,
            'disabilities' : profile.disabilities,

            'box11' : profile.box11,
            'box12' : profile.box12,
            'box13' : profile.box13,
            'box14' : profile.box14,
            'box15' : profile.box15,
            'box16' : profile.box16,
            'box17' : profile.box17,
            'box18' : profile.box18,
            'box19' : profile.box19,
            'box110' : profile.box110,
            'box111' : profile.box111,
            'box112' : profile.box112,

            'box21' : profile.box21,
            'box22' : profile.box22,
            'box23' : profile.box23,
            'box24' : profile.box24,
            'box25' : profile.box25,
            'box26' : profile.box26,
            'box27' : profile.box27,
            'box28' : profile.box28,
            'box29' : profile.box29,
            'box210' : profile.box210,
            'box211' : profile.box211,
            'box212' : profile.box212,

            'father_name' : profile.father_name,
            'father_occupation' : profile.father_occupation,
            'mother_name' : profile.mother_name,
            'mother_occupation' : profile.mother_occupation,
            'contact1' : profile.contact1,
            'contact2' : profile.contact2,
            'sibiling_count' : profile.sibiling_count,
            'family_status' : profile.family_status,
            'properties' : profile.properties,
            'anydetails' : profile.anydetails,

            'expected_qualification' : profile.expected_qualification,
            'expected_place' : profile.expected_place,
            'expected_income' : profile.expected_income,
            'expected_caste' : profile.expected_caste,
            'expected_subcaste' : profile.expected_subcaste,
            'age_difference' : profile.age_difference,
            'expected_height' : profile.expected_height,
            'expected_weight' : profile.expected_weight,
            'expectations' : profile.expectations
        })
    return jsonify(profile_response)

