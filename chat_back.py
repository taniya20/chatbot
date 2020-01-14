#Chatbot backend
# -*- coding: cp1252 -*-

def chatbot(string):
    
    
    #list=str.split(str)
    
    s=string.find("where")
    y=string.find("jamia millia islamia")
    u=string.find("jmi")
    sa=string.find("what")
    a=string.find("vision")
    mi=string.find("mission")  
    b=string.find("academics record")
    b1=string.find("national ranking")
    b2=string.find("ranking")
    s1=string.find("full form")
    c=string.find("faculty")
    c1=string.find("faculties")
    v=string.find("vice chancellor")
    v1=string.find("vice chancellor of jmi")
    v2=string.find("contact")
    w=string.find("website")
    c2=string.find("courses")
    c3=string.find("courses of jmi")
    c4=string.find("jmi courses")
    c5=string.find("M54")
    c6=string.find("fees")
    c7=string.find("mca fees")
    c8=string.find("MCA fees")
   
    create=string.find("creator");
    dev=string.find("developer");
    who=string.find("who");
    hi=string.find("hi")
    he=string.find("hello")
    re=string.find("reach")
    ho=string.find("how")
   
    if s >= 0:
        s= "Jamia Millia Islamia is located near JAMIA MILLIA ISLAMIA metro station, Maulana Mohammad Ali Jauhar Marg, Jamia Nagar, New Delhi-110025."
    
    elif y >= 0:
        s= "Jamia Millia Islamia is located near JAMIA MILLIA ISLAMIA metro station, Maulana Mohammad Ali Jauhar Marg, Jamia Nagar, New Delhi-110025.\n       It has been established in 1920,originally at Aligarh in United Provinces which in 1925 initially moved to Karol Bagh, Delhi and later built up in Jamia Nagar.       \nIn 1988, it became the Central University by an Act of Parliament since then it is expanding in different directions achieving the new dimensions."

    elif y >= 0:
        s= "Jamia Millia Islamia is located near JAMIA MILLIA ISLAMIA metro station, Maulana Mohammad Ali Jauhar Marg, Jamia Nagar, New Delhi-110025.\n\nIt has been established in 1920,originally at Aligarh in United Provinces which in 1925 initially moved to Karol Bagh, Delhi and later built up in Jamia Nagar.\n\nIn 1988, it became the Central University by an Act of Parliament since then it is expanding in different directions achieving the new dimensions."      
        
    elif s >= 0 and (u >0 or y>0):
        s= "Jamia Millia Islamia is located near JAMIA MILLIA ISLAMIA metro station, Maulana Mohammad Ali Jauhar Marg, Jamia Nagar, New Delhi-110025."

    elif sa>=0 or u>=0:
        s = "JMI is a Public Central University.\n\nIt has been established in 1920,originally at Aligarh in United Provinces which in 1925 initially moved to Karol Bagh,Delhi and later built up in Jamia Nagar.\n\nToday, Jamia Millia Islamia is an 'A' grade Central University accredited by NAAC and is an ensemble of a multiayered educational system\n\nwhich covers all aspects of schooling, under-graduate and post-graduate education."


    elif sa>=0 and (y>0 or u>0):
        s = "JMI is a Public Central University.\n\nIt has been established in 1920,originally at Aligarh in United Provinces which in 1925 initially moved to Karol Bagh,Delhi and later built up in Jamia Nagar.\n\nToday, Jamia Millia Islamia is an 'A' grade Central University accredited by NAAC and is an ensemble of a multiayered educational system\n\nwhich covers all aspects of schooling, under-graduate and post-graduate education."

    elif a >= 0:
        s= "To create a human universe that offers inclusiveness,equity,fellowship,justice and peace for everyone."
        
    elif a >= 0 and u >=0:
        s= "To create a human universe that offers inclusiveness, equity, fellowship, justice and peace for everyone."

    elif mi >=0:
         s= "\n-- To serve the nation through quality teaching and research by producing competent\n-- skilled and sensitive human resource that would catalyze enrichment of physical and human environment.\n-- To be a world-class teaching cum research university seeking the establishment of a collaborative research environment through free exchange of ideas.\n-- To strive for the sustainable development of society and ensure optimum capacity building.\n-- To attract and retain diverse creative minds for the actualization of institutional objectives."
         

    elif b >=0:
        s= "\n -Almost 18000 of students admitted in various programmes excluding 3490 school students.\n-241 Foreign students.\n-34.7% Female students and 65.3% male students.\n- 317 Students awarded Merit Scholarship."
       
       # s= "• JMI is the lead institute and Chair for thematic group BRICS Studies: BRICS Network University."
        #s= "• University has received R&D Grant of Rs. 15 crores under DST-PURSE Scheme."
        #s= "• 15 faculty members are INSA Fellow and three faculty members are JC Bose Fellows."
        #s= "• Four faculty members are on Visiting Professorship of foreign universities."

    elif b1 >=0 or b2 >=0:
        s= "• The University is placed at 12th position among the Universities and 6th position among the central\nUniversities of the country as per MHRD-NIRF (National Institute Ranking Framework) 2017.\n• Faculty of Engg & Technology is placed 20th position as per MHRD-NIRF 2017.\n• Faculty of Law has been ranked as No. 1 in India Today Survey 2017 at national level.\n• The University is ranked in 800- 1000 bracket in world ranking by Times Higher Education."
        
  

    elif s1 >=0:
        s= "JMi stands for JAMIA MILLIA ISLAMIA"

    elif c >=0:
        s= "Faculty of Humanities and Languages\n           Faculty of Social Sciences\n           Faculty of Natural Sciences\n           Faculty of Education\n           Faculty of Engineering & Technology\n           Faculty of Law\n           Faculty of Architecture and Ekistics\n           Faculty of Fine Arts\n           Faculty of Dentistry\n           Centres of Studies"

    elif c1 >=0:
        s= "Faculty of Humanities and Languages\n           Faculty of Social Sciences\n           Faculty of Natural Sciences\n           Faculty of Education\n           Faculty of Engineering & Technology\n           Faculty of Law\n           Faculty of Architecture and Ekistics\n           Faculty of Fine Arts\n           Faculty of Dentistry\n           Centres of Studies"

    elif v>=0:
        s= "Vice-Chancellor of jamia millia islamia is NAJMA AKHTAR)."

    elif v1>=0:
        s= "Vice-Chancellor of jamia millia islamia is NAJMA AKHTAR)."    
 
    elif v2>=0:
        s= "The contact no. is 011 26981717"

    elif w>=0:
        s= "Website of Jamia Millia Islamia is : jmi.ac.in"
        
    elif c2>=0 or c3>=0 or c4>=0:
        s= "\nB.A.(Hons) (Turkish Language & Literature)\nAdvanced Diploma in Turkish\nDiploma in Turkish\nDiploma in Korean Language\nM.A.(Arabic)\nM.A.(English)\nB.A.(Hons)(English)\nM.A.(Hindi)\nM.Com.(Business Management)\nB.B.A.(Bachelor of Business Administration)\nB.A.(Hons)(Economics)\nB.Sc.\nM.Sc.(Bio sciences)\nM.Sc.(Bioinformatics)\nM.C.A\nP. G. Diploma in Computer Application\nM.A./M.Sc.(Geography)\nB.A./B.Sc.(Hons) (Geography)\nM.Sc. (Physics)" 


    elif c5>=0:
        s= "M.C.A(MASTERS IN COMPUTER APPLICATIONS)"

    elif c6>=0 or c7>=0 or c8>=0:
        s= "Rs.8,400 per year"


    
    elif hi>=0 or he>=0:
        s= "Hello! How can i help you?"
    elif v>=0:
        s = "The contact no. is +91-11-27666702. The email id is info@cic.du.ac.in"
        s = "However you can ask anything here and i will leave a reply to your email id later"
    elif create >= 0 or dev >= 0 or (who>=0 and dev>=0) or (who>=0 and create>=0):
        s="Creators /Developer of this Chatbot are Kamal Ranjan and Taniya Aslam"

    else:
        s= "Sorry! I need to think over it. Please leave your email address and I'll respond back"

    return s
