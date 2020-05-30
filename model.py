import sqlalchemy as sa
from sqlalchemy_mixins import AllFeaturesMixin
from app import app, db

class BaseModel(db.Model, AllFeaturesMixin):
    __abstract__ = True
    pass

BaseModel.set_session(db.session)

class Profiles(BaseModel):

    id = sa.Column(sa.Integer, primary_key=True)

    # Personal details
    imageUrls = sa.Column(sa.Text)
    name = sa.Column(sa.String(30))
    email = sa.Column(sa.String(30), unique=True, nullable=True)
    password = sa.Column(sa.String(18))
    gender = sa.Column(sa.Boolean)
    dob = sa.Column(sa.Date)
    birth_time = sa.Column(sa.Time)
    birth_place = sa.Column(sa.String(30))
    religion = sa.Column(sa.String(30))
    caste = sa.Column(sa.String(30))
    subcaste = sa.Column(sa.String(30))
    gothram = sa.Column(sa.String(30))
    star = sa.Column(sa.String(30))
    qualification = sa.Column(sa.String(30))
    job = sa.Column(sa.String(30))
    workplace = sa.Column(sa.String(30))
    income = sa.Column(sa.Numeric())
    height = sa.Column(sa.Float(5))
    weight = sa.Column(sa.Float(5))
    mother_tongue = sa.Column(sa.String(30))
    known_language = sa.Column(sa.Text)
    nativity = sa.Column(sa.String(30))
    marital_status = sa.Column(sa.Boolean)
    talents = sa.Column(sa.Text)
    hobbies = sa.Column(sa.Text)
    vehicle_driving = sa.Column(sa.String(30))
    disabilities = sa.Column(sa.String(30))

    # Horoscope details
    box11 = sa.Column(sa.String(30), nullable=True)
    box12 = sa.Column(sa.String(30), nullable=True)
    box13 = sa.Column(sa.String(30), nullable=True)
    box14 = sa.Column(sa.String(30), nullable=True)
    box15 = sa.Column(sa.String(30), nullable=True)
    box16 = sa.Column(sa.String(30), nullable=True)
    box17 = sa.Column(sa.String(30), nullable=True)
    box18 = sa.Column(sa.String(30), nullable=True)
    box19 = sa.Column(sa.String(30), nullable=True)
    box110 = sa.Column(sa.String(30), nullable=True)
    box111 = sa.Column(sa.String(30), nullable=True)
    box112 = sa.Column(sa.String(30), nullable=True)
    
    box21 = sa.Column(sa.String(30), nullable=True)
    box22 = sa.Column(sa.String(30), nullable=True)
    box23 = sa.Column(sa.String(30), nullable=True)
    box24 = sa.Column(sa.String(30), nullable=True)
    box25 = sa.Column(sa.String(30), nullable=True)
    box26 = sa.Column(sa.String(30), nullable=True)
    box27 = sa.Column(sa.String(30), nullable=True)
    box28 = sa.Column(sa.String(30), nullable=True)
    box29 = sa.Column(sa.String(30), nullable=True)
    box210 = sa.Column(sa.String(30), nullable=True)
    box211 = sa.Column(sa.String(30), nullable=True)
    box212 = sa.Column(sa.String(30), nullable=True)

    # Family details
    father_name = sa.Column(sa.String(30))
    father_occupation = sa.Column(sa.String(30))
    mother_name = sa.Column(sa.String(30))
    mother_occupation = sa.Column(sa.String(30))
    contact1 = sa.Column(sa.String(30), unique=True, nullable=True)
    contact2 = sa.Column(sa.String(30), unique=True, nullable=True)
    sibiling_count = sa.Column(sa.Integer, nullable=True)
    family_status = sa.Column(sa.String(30), nullable=True)
    properties = sa.Column(sa.Text)
    anydetails = sa.Column(sa.Text)

    # Partner Expectations
    expected_qualification = sa.Column(sa.Text, nullable=True)
    expected_place = sa.Column(sa.Text, nullable=True)
    expected_income = sa.Column(sa.Numeric())
    expected_caste = sa.Column(sa.String(30))
    expected_subcaste = sa.Column(sa.String(30))
    age_difference = sa.Column(sa.String(30))
    expected_height = sa.Column(sa.Float(5))
    expected_weight = sa.Column(sa.Float(5))
    expectations = sa.Column(sa.Text)