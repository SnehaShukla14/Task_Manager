JWT Authentication Explanation
JWT (JSON Web Token) is the method we used to securely authenticate users in the API (no sessions, perfect for mobile/web clients).
How it works in the project

(JSON WEB TOKEN) JWT Authentication

JWT stands for JSON Web Token. It's a secure way to authenticate users in APIs without using traditional sessions. Project uses djangorestframework-simplejwt for this.

How JWT Works in Task Manager

Endpoint: POST /api/auth/token/
Body: {"username": "alice", "password": "alice123"}
Below is the screenshot for it and tested in postman as well
<img width="1920" height="1026" alt="Screenshot (314)" src="https://github.com/user-attachments/assets/a3e489aa-4016-4f7a-b275-131cb64e678a" />
<img width="1920" height="1080" alt="Screenshot (315)" src="https://github.com/user-attachments/assets/da163d8d-d6a4-47ae-b7cf-a06b0cc78575" />
<img width="1920" height="1080" alt="Screenshot (318)" src="https://github.com/user-attachments/assets/ef243d11-c8e5-4b5f-8b9f-65fa8055b368" />
<img width="1920" height="1080" alt="Screenshot (318)" src="https://github.com/user-attachments/assets/ef243d11-c8e5-4b5f-8b9f-65fa8055b368" />

Registration
POST /api/auth/register/
Creates a new user (sneha/alice/bob) and automatically adds them to the "User" group.
Screenshot in Django Rest Framework and Postman
<img width="1920" height="1020" alt="Screenshot (308)" src="https://github.com/user-attachments/assets/78411a90-0e4f-49bd-aed5-0e93f3b91c4c" />
<img width="1920" height="1080" alt="Screenshot (288)" src="https://github.com/user-attachments/assets/f63bec5c-5838-4db4-a81f-77c79f2b34b8" />

RBAC (Role-Based Access Control) Explanation
RBAC means different users have different permissions based on their role/group.
Screenshots perfectly demonstrate RBAC:

Alice's view
Logged in as alice
Sees only 1 task (the one she created)
Does not see Bob's task → correct!

Bob's view
Logged in as bob
Sees only 1 task (his own)
Does not see Alice's task → correct!

Sneha's view
Logged in as admin
Sees both 2 tasks (Alice's + Bob's) → correct!
<img width="1920" height="1024" alt="Screenshot (291)" src="https://github.com/user-attachments/assets/185205c0-cc33-4dd6-a787-7b97c47ee9fe" />
<img width="1920" height="1031" alt="bob" src="https://github.com/user-attachments/assets/e83149e4-6ace-43b2-9284-54b0226f17b1" />
<img width="1920" height="1031" alt="Screenshot (293)" src="https://github.com/user-attachments/assets/a8d69149-ae63-4b75-b994-2496ea109d03" />
<img width="1920" height="1026" alt="Screenshot (294)" src="https://github.com/user-attachments/assets/6b414c3c-8062-4a4c-9c87-6c2281ac4f9e" />

Login through Username and Password using Django Rest Framework
<img width="1920" height="1026" alt="Screenshot (297)" src="https://github.com/user-attachments/assets/579baf76-c246-4a68-a09e-b55a122d167b" />


Screenshot for tasks/ users lists:
<img width="1920" height="1026" alt="Screenshot (316)" src="https://github.com/user-attachments/assets/af331dce-cb42-4497-93d6-c3b9f43fd385" />

Django Admin related screenshots
<img width="1920" height="1020" alt="Screenshot (302)" src="https://github.com/user-attachments/assets/b8411623-412c-47b5-a45a-a3ff53d44e7b" />
<img width="1920" height="1035" alt="Screenshot (303)" src="https://github.com/user-attachments/assets/37d2bfb0-eda7-4a1a-8966-f4e7d915f937" />



