Flask Setup
1. Begin by creating a new project directory:
    > mkdir ofir
    > cd ofir

2. Within "ofir", place the CSV file 'churn_case_data.csv' and create a new directory called "server".
   Then, inside the "server" directory, create and activate a virtual environment :
    > cd server
    > python -m venv env
    > env\Scripts\activate
    (The above commands may differ depending on your environment.)

3. Install Flask along with the Flask-CORS extension: (still within 'server')
    > pip install Flask Flask-Cors

4. Add the app.py file 'server' folder

5. Run the app:
    >> (env)$ python app.py

6. To test, point your browser at http://localhost:5000/customers. You should see data from the CSV file as JSON

7. install vue cli globally 
    > npm install -g vue-cli

8. Then, within "ofir" (project's root folder), run the following command to initialize a new Vue project called client with the webpack config:
    > vue init webpack client
    (
        ? Project name client
        ? Project description A Vue.js project
        ? Author Ofir <nesher123@gmail.com>
        ? Vue build standalone
        ? Install vue-router? Yes
        ? Use ESLint to lint your code? No
        ? Set up unit tests No
        ? Setup e2e tests with Nightwatch? No
    )
    > cd client

9. inside 'client' folder, replace the 'src' folder with the downloaded 'src' folder

10. > npm install bootstrap-vue@2.0.0-rc.11 axios@0.18.0 bootstrap@4.1.1 --save
    > npm install

11. > npm start (still within 'client')

12. from another Terminal, go into 'server' directory and run:
    > python app.py

13. open http://localhost:8080 and enjoy!
