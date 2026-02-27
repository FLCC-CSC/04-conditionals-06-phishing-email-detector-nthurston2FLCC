# FILE NAME - phishing_email_detector.py

# NAME: Nicholas Thurston
# DATE: 2/26/2026
# BRIEF DESCRIPTION:  Phish Detector



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    def phish_detector():
        
        # ask user for subject line
        subject = str(input('Enter the email subject line: '))
        subject_upper = subject.upper()

        # high risk indicators
        high_risk = ['URGENT','IMMEDIATE ACTION REQUIRED']

        # medium risk indicators
        med_risk = ['WIN','FREE']

        print('SECURITY ASSESSMENT:\n')

        # logic to detect phish
        if any(risk in subject_upper for risk in high_risk):
            print('HIGH RISK: Possible phishing attempt.')
            print('------------------------')
            print(f'Analyzed subject: {subject}')
        elif any(risk in subject_upper for risk in med_risk):
            print('MEDIUM RISK: Suspicious offer detected.')
            print('------------------------')
            print(f'Analyzed subject: {subject}')
        else:
            print('LOW RISK: Verify legitimacy with sender')

    phish_detector()
main()








########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
Enter the email subject line: Meeting on Friday

SECURITY ASSESSMENT:
No phishing indicators detected.
------------------------
Analyzed subject: "Meeting on Friday"
'''

'''
Enter the email subject line: URGENT REQUEST FOR BANK TRANSFER

SECURITY ASSESSMENT:
HIGH RISK: Possible phishing attempt.
------------------------
Analyzed subject: "URGENT REQUEST FOR BANK TRANSFER"
'''

'''
Enter the email subject line: All I do is win win win no matter what

SECURITY ASSESSMENT:
MEDIUM RISK: Suspicious offer detected.
------------------------
Analyzed subject: "All I do is win win win no matter what"
'''

'''
Enter the email subject line: Did you request a password reset?

SECURITY ASSESSMENT:
LOW RISK: Verify legitimacy with sender.
------------------------
Analyzed subject: "Did you request a password reset?"
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Was using `in` difficult or was it natural?


It was pretty natural. I like it because it saves a lot of hassle. I also wanted to simplify the code a bit and used the "any" function to check for the strings.




'''



########################################
#            ATTESTATION
########################################

'''

Please gauge your utilization of AI on the following spectrum. Place an "X" in front
of the appropriate response. Only choose one of the following:

[ ] I did not use AI at all for this lab.
[ ] I wrote the initial draft of the software but had AI help me make it better.
[ ] I fed the lab description to AI and had it generate a response but I modified it.
[ ] AI created the entire program for me.



It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[ ] I'm solid. Totally got it.

'''
