# pizzapi

A rest api in Django and DRF to  order and manage a pizza shop  - an interview  solution

# Running the project locally

1. Clone the project using `git clone`
2. Enter the project directory i.e `cd pizzapi`
3. Create a file named `.env.dev` and copy the contents of `.env.dev.sample` to the newly created `.env.dev`
4. While inside the `pizzapi` directory with docker and docker-compose installed, run `docker-compose build` to build the containers. This might take a few minutes
5. If you want to populate the database with some test data, run `docker-compose exec web python manage.py loaddata`
6. Start the project with the command `docker-compose up -d`
7. Visit http://localhost:8000/api/v1/docs to get started with the browsable api

# Testing

Run `docker-compose exec web python manage.py test`
