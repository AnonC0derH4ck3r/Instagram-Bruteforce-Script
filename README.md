# Instagram Bruteforce Script
This is a basic yet working script which you can use to bruteforce the instagram.
It might give false response, as the meta has updated their security measures.

# How does it work?
Provide a username and password to the *InstaLogin* function.
It makes a get request to capture the csrf_token from the page and loops every line,
of the credential file to hit and try the email and password combinations.

# Note
Make sure your credentails file is a *.txt* file and it has the combinations of email and password in the following format:
    victim_email@mail.com:victim_password

However, you can edit that out if you know python programming.

# Disclaimer
Yeah, you think I'll miss this part?
Hacking into the account for which you don't have explicit permission is illegal. You CAN land in jail
and I won't be responsible for your actions. use it for testing and education purpose.

Happy Hacking ;)