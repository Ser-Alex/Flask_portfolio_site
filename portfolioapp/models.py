from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __unicode__(self):
        return self.username


class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120))
    image = db.Column(db.String(255), nullable=False)


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return self.image


class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(120))
    client = db.Column(db.String(120))
    date = db.Column(db.Date)
    location = db.Column(db.String(120))
    image_1 = db.Column(db.String(255))
    image_2 = db.Column(db.String(255))
    image_3 = db.Column(db.String(255))
    image_4 = db.Column(db.String(255))
    image_5 = db.Column(db.String(255))
    image_6 = db.Column(db.String(255))
    image_7 = db.Column(db.String(255))
    image_8 = db.Column(db.String(255))
    image_9 = db.Column(db.String(255))
    image_10 = db.Column(db.String(255))


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    image = db.Column(db.String(255), nullable=False)
    text_name = db.Column(db.String(64), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)


class Skill(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    skill = db.Column(db.String(64), nullable=False)
    percent = db.Column(db.Integer(), nullable=False)


class About(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    text_name = db.Column(db.String(64), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255), nullable=False)

