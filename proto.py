import numpy as np



from pylatex import Document, Section, Subsection, Subsubsection, Command, Itemize
from pylatex.section import Paragraph
from pylatex.utils import italic, NoEscape
import datetime
import os

def report(doc, subject="Project"):
    project = input(subject + ": ")
    person = input(subject + " Reporter: ")
    report = input("Report: ")
    with doc.create(Subsubsection(project + " -- " + person)):
        doc.append(report)
        

def announcements(doc):
    with doc.create(Itemize()) as itemize:
        announcement = input("Annoucement Section: ")
        if announcement == 'y':
            while announcement == 'y':
                new_announcement = input("Announcement: ")
                itemize.add_item(str(new_announcement))
                announcement = input("More announcements: ")
            itemize.append(Command("ldots"))

def add_business(doc):
    business = input("Business on agenda: ")
    
    with doc.create(Subsubsection(business)):
        pass

def run_business(doc, type_of_business="Old Business"):
    business_section = input("More " + type_of_business + ": ")
    while business_section == 'y':
        add_business(doc)
        move_section = input("More motions? ")
        
        with doc.create(Itemize()) as itemize:
        
            while move_section == 'y':
                itemize.add_item(move(doc))
                move_section = input("More motions? ")
            itemize.append(Command("ldots"))
        business_section = input("More " + type_of_business + ": ")

def move(doc):
    person = input("Proposer: ")
    motion = input("Motion: ")
    second = input("Is there a second?: ")
    if second == 'n':
        return person  + " moved to " + motion + " but the motion failed because of there was a lack of a second."
    else:
        discussion = input("Did the motion fail (f), remain (r), or amend (a) during discussion: ")
        amended = False
        amendedMover = ""
        amendedMotion = ""
        if discussion == 'f':
            return person + "'s motion to " + motion + " failed during discussion"
        elif discussion == 'a':
            amended = True
            amendedMotion = input("Amended Motion: ")
            amendedMover = input("Who moved to amend motion? ")
            
        vote = input("Yay (y) or nay (n): ")
        writeup = "%s moved to %s. %s seconded the motion." % (person, motion, second) 
        if amended:
            writeup += " After discussion, %s moved to amend the motion to %s. It was seconded." % (amendedMover, amendedMotion)
        if vote == 'y':
            writeup += " The club voted in the affirmative."
        else:
            writeup += " The club rejected the motion in a vote."
        return writeup

if __name__ == '__main__':
    members = ["Hope Berry", "Shepard Berry", "Peter Chacko", "Thomas Chacko", "Isabel Bettencourt", "Grace Bettencourt", "Claire Bettencourt", "Sara Bettencourt"]
    doc = Document(datetime.date.today().strftime("%B %d, %Y") + " 4-H Business Meeting")
    doc.preamble.append(Command('title', r'4H Business Meeting'))
    doc.preamble.append(Command('author', r'Peter Chacko'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))
    
    current_time = str(datetime.datetime.now())        
    # Call to Order
    with doc.create(Section('Call to Order')):
        president = input("President: ")
        prayer = input("Prayer: ")

        us_pledge = input("US Pledge: ")
        four_h_pledge = input("4-H Pledge: ")
        tx_pledge = input("TX Pledge: ")
        
        vp = input("Vice President: ")
        inspiration_content = input("Summary of inspiration: on ")
       
        print("Roll Call: ") 
        members_in_attendance = ""
        for index, member in enumerate(members, 1):
            here = input("--" + member + " ")
            if here != 'n':
                # If last one, use oxford comma
                if index == len(members):
                    members_in_attendance += "and " + member 
                else:
                    members_in_attendance += member + ", "
        guests = input("New members or guests: ")

        introduction = "President %s started the meeting at %s. %s led us in prayer. %s led the US Pledge, %s led the 4-H Pledge, and %s led the Texas Pledge. %s gave an inspiration on %s. %s were in attendance. " % (president, current_time, prayer, us_pledge, four_h_pledge, tx_pledge, vp, inspiration_content, members_in_attendance)

        if guests != 'n':
            introduction += guests + " were new memebers or guests."
        else:
            introduction += "There were no new members or guests."
        doc.append(introduction)
    
    # Reports    
    with doc.create(Section('Reports')):
        
        # Officer reports
        with doc.create(Subsection('Officer')): 
            secretary_report_approved = input("Old minutes approved: ")
            

            treasurer = input("Treasurer: ")
            balance = input("Treasury Balance: ")
            tr_notes = input("Notes from treasurery report: ")
            
            hlth_sfty_officer = input("Health and Safety Officer: ")
            hlth_sfty_report = input("Health and Safety Topic: on")

            cc_delegate = input("County Council Delegate: ")
            cc_report = input("County Council Report: such as ")
            
            officer_reports = ""
            if secretary_report_approved != 'y':
                officer_reports = "Correction to the minutes: " + secretary_report_approved
            else:
                officer_reports = "The minutes were approved as read."
            officer_reports += " The financial report was given by %s. We have %s in the bank account. %s %s gave the Health and Safety Report on %s. %s gave an update on the County Council such as %s." % (treasurer, balance, tr_notes, hlth_sfty_officer, hlth_sfty_report, cc_delegate, cc_report)
            doc.append(officer_reports)        
        
        # Project Reports 
        with doc.create(Subsection('Projects')) as proj:
            project_section = input("Any Projects?  ")
            while project_section == 'y':
                report(doc, subject="Project")
                project_section = input("More Projects? ")
        
        # Committee Reports
        with doc.create(Subsection('Committees')) as committee:
            committee_section = input("Any Committees? ")
            while committee_section == 'y':
                report(doc, subject="Committee")
                committee_section = input("More Committees? ")
    
    # Business
    with doc.create(Section("Business")):
        
        # Old Business
        with doc.create(Subsection("Old Business")):
            run_business(doc, type_of_business="Old Business") 
        # New Business
        with doc.create(Subsection("New Business")):
            run_business(doc, type_of_business="New Business") 
    
    with doc.create(Section("Announcements")):
        announcements(doc)        
    

    doc.generate_pdf(datetime.date.today().strftime("%B %d, %Y"), clean_tex=False)
    tex = doc.dumps()


