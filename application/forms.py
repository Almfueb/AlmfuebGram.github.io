from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, EmailField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from application.utils import exists_email, not_exists_email, exists_username
    

class LoginForm(FlaskForm):
    username            = StringField("username", validators=[DataRequired()])
    password            = PasswordField("password", validators=[DataRequired()])
    submit              = SubmitField("Login")

class SignUpForm(FlaskForm):
    username            = StringField("username", validators=[DataRequired(), Length(min=4, max=16), exists_username])
    fullname            = StringField("full name", validators=[DataRequired(), Length(min=4, max=16)])
    email               = EmailField("email", validators=[DataRequired(), Email(), exists_email])
    password            = PasswordField("password", validators=[DataRequired(), Length(min=8)])
    confirm_password    = PasswordField("confirm password", validators=[DataRequired(), Length(min=8), EqualTo("password")])
    submit              = SubmitField("sign up")

    
class EditProfileForm(SignUpForm):
    username            = StringField("username", validators=[DataRequired(), Length(min=4, max=16)])
    fullname            = StringField("fullname", validators=[DataRequired(), Length(min=4, max=16)])
    password            = None    
    confirm_password    = None
    email               = None
    bio                 = StringField("bio")
    submit              = SubmitField("Update Profile")
    profile_pic         = FileField("Profile Picture", validators=[FileAllowed(["jpg", "png", "jpeg"])])


class ResetPasswordForm(FlaskForm):
    old_password        = PasswordField("old password", validators=[DataRequired(), Length(min=8)])
    new_password        = PasswordField("new password", validators=[DataRequired(), Length(min=8)])
    confirm_new_password = PasswordField("confirm new password", validators=[DataRequired(), Length(min=8), EqualTo("new_password")])
    submit              = SubmitField("Reset Password")

class ForgotPasswordForm(FlaskForm):
    email               = EmailField("email", validators=[DataRequired(), not_exists_email])
    # recaptcha           = RecaptchaField()
    password = PasswordField("new password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("confirm new password", validators=[DataRequired(), Length(min=8), EqualTo("password")])
    submit              = SubmitField("Send Link Verification To Email")

class VerificationResetPasswordForm(FlaskForm):
    password = PasswordField("new password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("confirm new password", validators=[DataRequired(), Length(min=8), EqualTo("password")])
    submit = SubmitField("Reset password")

class CreatePostForm(FlaskForm):
    post_pic            = FileField("Picture", validators=[DataRequired(), FileAllowed(["jpg", "png", "jpeg"])])
    caption             = TextAreaField("Caption")
    submit              = SubmitField("Post")

class EditPostForm(FlaskForm):
    caption             = StringField("caption")
    submit              = SubmitField("Update")