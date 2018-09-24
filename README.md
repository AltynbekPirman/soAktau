Hello there, old friend!!!
This is docs for Django backend for soAktau

Well, here we goooooo:

NEWS & Announcements:

*GET /api/v1.0/news?lang={language-code}             - list of news, can be filtered by language(kaz or rus)

*GET /api/v1.0/announcements?lang={language-code}    - list of announcements, can be filtered by language(kaz or rus)



FAQ:

*POST /api/v1.0/questions/{language-code}  - POST question; example input   {"question": "is this a question", 
                                                                             "language": {"code": "rus"} }

*GET /api/v1.0/questions/{language-code}        - list of questions in kaz or rus

*GET /api/v1.0/questions/{language-code}/{id}   - get question detail with answers


Admin:
*GET /admin         - django's admin page