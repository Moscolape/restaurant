# WORKING-RESTAURANT.PY

This is a program created for an imaginary mobile ordering application for a restaurant...

### Program Features

When this program is run, the user is given the following options: 
1- Sign up 
2- Sign in 
3- Quit application 


### Prerequisites for Sign-up

1. The signup process will not be successful until:
2. The mobile number has 10 digits starting with 0.
3. The Password must initiate with alphabets followed by either one of @, & and ending with numeric. (For Example: Sam@0125, Sam&25)
4. The password confirmation matches the initial entered password.
5. The DOB is in the format DD/MM/YYYY
6. The user is at least 21 years old. The age should be calculated based on the year 
entered in the DOB (Only consider year).

If any of the above-mentioned condition is not fulfilled; the sign-up process should fail, and 
descriptive message should be displayed for the user explaining what has gone wrong and 
providing hints on the correct expected input. The program should keep asking the user to 
re-enter his details as long as one or more of the input fields are not correctly entered. If all 
fields are entered successfully, the program should stop asking the user to re-enter his 
details and display a message that the signup process has been completed successfully...


### Prerequisites for Log-in

The Application must save the User’s information of all the Successful Signups in the appropriate data 
structure for verification purposes. During the login the program must verify the user id and password before confirming the user for successful login. Once the login is successful the user’s name must be displayed in the greeting message. After the login the user must be asked the options to sign-out and reset the password.

If the user has not signed up with the entered username (mobile number), the program must ask the 
user to sign up first. If the user selects the Sign-out option, the user is back to the home screen with the options of 
Signup, Sign in and Quit Application. 
