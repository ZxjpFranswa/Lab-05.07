# Lab-05.07 - PAYAGO - OBA

1. Activity Description
GitHub OAuth & API Security Lab
A Flask-based implementation demonstrating the OAuth 2.0 Authorization Code Flow using GitHub as the Identity Provider (IdP).

2. Prerequisites
Python 3.14
A GitHub account

3. Installation & Setup
Clone the repo: git clone/ or install the file manually from github
Install dependencies: pip install -r requirements.txt

4.How to Run
app.py
visit http://localhost:5000. 

5. API Documentation (The Routes)
GET /: The landing page/login page.
GET /login: Redirects the user to GitHub for authorization.
GET /callback: Handles the response from GitHub and swaps the code for a token.
GET /profile: [Protected] Displays JSON user data if a session exists.
GET /logout: Clears the session.

# Critical Thinking

i. What happens when a user accesses /profile without logging in?
- for this one, if they try to go straight to the /profile route but they are not logged in yet, they will just get bounced back! The system will usually block them and throw an "Unauthorized" error (like a 401 status), or it will just automatically redirect them back to the login page. Basically, no ID, no entry!

ii. What data is returned after successful login?
Once they successfully log in, the server will usually give back an access token (like a JWT) so their session stays active. Aside from that, it also returns their basic user details—like their name, email address, and user ID—so we have something to display on the frontend when they check their profile.

iii. Why is OAuth considered more secure than traditional login?
OAuth is way more secure because we don't even need to handle or save the user's passwords in our own database anymore. It's like we are just letting Google or Facebook do the heavy lifting and security checks for us. They just give us a token to prove the user is legit. So, even if our database gets compromised (knock on wood!), the users' actual passwords are super safe.

iv. What challenges did you encounter?
The hardest part for me was probably dealing with the CORS errors; it just kept blocking my requests at first. Also, setting up the OAuth client IDs and secret keys in the developer console was a bit overwhelming. I really had to double-check the redirect URIs because even just one small typo and the whole flow just won't work!

v. What did you learn from this activity?

I really learned a lot here! I finally understood how the whole authentication flow actually works, especially how the tokens are passed back and forth between the frontend and the backend. It really made me appreciate how important security and routing are when building web apps. It was a bit of a headache at first, but super fulfilling once the login finally worked!
