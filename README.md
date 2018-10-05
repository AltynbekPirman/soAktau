Hello there, old friend!!!
This is docs for Django backend for soAktau

Well, here we goooooo:

SERVICES:

*GET /api/v1.00/services                                         - list of services, grouped by language 

*GET /api/v1.00/services/{service_id}                            - services detail, list of sub-services for service with given id grouped by language

*GET /api/v1.00/services/{service_id}/{sub_service_id}              - list of titles(sub_sub_services), for given service and sub_service ids

*GET /api/v1.00/services/{service_id}/{sub_service_id}/{title_id}   - posts :)



NEWS & Announcements:

*GET /api/v1.00/news?lang={language-code}             - list of news, can be filtered by language(kaz or rus)

*GET /api/v1.00/announcements?lang={language-code}    - list of announcements, can be filtered by language(kaz or rus)



FAQ:

*POST /api/v1.00/questions/{language-code}  - POST question; example input   {"question": "is this a question", 
                                                                             "language": {"code": "rus"} }

*GET /api/v1.00/questions/{language-code}        - list of questions in kaz or rus

*GET /api/v1.00/questions/{language-code}/{id}   - get question detail with answers


Admin:
*GET /admin         - django's admin page
