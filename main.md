**Get Request**

1. Get request hum api se data rrecived kret h.

2. Post main hum api ko data dete h aur phir recived krte h.

**Why We Need Schema**

1. it's a pain to get all the values from the body.

2. The client can shed whatever data they want.

3. The data isn't getting validated.

4. We ultimately want to force the client to send data in a schema that we except

**CURD**

Create --> /posts --> @app.post("/posts")

Read --> /posts/:id --> @app.get("/posts/{id}")

     --> /posts --> @app.get("/posts")

Updates --> PUT/PATCH --> /posts/:id --> @app.put("/posts/{id}")

Delete  --> /posts/:id --> @app.delete("/posts/{id}")

**Primary Key**

1. ye harek table main rhega. aur wo hreak user ka ek unique rhega dont be dubliacte just like id

**Oject Relational MApper(ORM)**

1. Layer of abstraction that sits between the database and us

2. We can perform all database operation throungh traditional python code. No more SQL.

* Hum direcly databasse se bat nhai krege fastapi main starder python code likege phir wo code ORM sql main convert kr dega. phir wo databse ko bjega.

**What can orm do**

1. Insteand of manually defineng tables in postgres, we can define as ython models.

2. Queries can be made exclsivly through pythin code. No SQL is nessary.

**Pydantic model**

1. What request look like .

imagine kro kii hum ek post bna rhe h to usme title rhna cahiye , str rhna cahoye ect e sab btatata h.

**Responce Model:**

1. What responce should looklike 

**Vote Models**

1. 