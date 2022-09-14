# Sharepoint
Platform for sharing goods
The website allows the user to give the donation in form of f.e. clothes, shoes etc to an
institution that needs those kind of things.

class LandingPage(View) enables us to see how many doanations were given and to what institution.
It shows the quantity of help donated to the foundations, non-governemental institutions and local raises.

class AddDonation(View) is a form to choose what kind of donation the user wants to give. he form enables easy categorisation and choise of the institution.

Function register_user allows us to register as a user.

class Login(View) is a mechanism to log in. Without it it is immpossible to add the donation.

class Logout(View) is the logout mechanism.

class Profile(View) enables the view of the user profile, available only for the logged in user.
It summarises the donations of the user and helps to manage the doantions.


