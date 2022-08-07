### Insta-Clone
Practicing fast-api with various frontends with a simple clone of instagram. Supports multiple users, uploading images (or linking to images), and commenting.

## How to run
With the power of pipenv, this is easy. Clone this repo, and run `pipenv install` which will get you up and running. You will need a `.env` file with at least `SECRET_KEY` defined (you can create this string yourself with something like `openssl rand -hex 32`), you can also optionally specify the DB address with `DATABASE_URL`).
Once that is done, you can run `pipenv shell` and then just start up the server with `uvicorn main:app --reload`.

## That's cool, but where do I see what calls to make?
By default, this should be on hosted on localhost and whatever port you specified (by default, this should be `8000`). You can then go to said address (ex `http://localhost:8000/docs`) with docs on the end and see what calls are available and their expected payload. You will need to create a user to get started making posts or uploading images. 

## Where do the images go?
Depends on the post- you can create a post with an absolute path (ex `https://best.image.com/images/catsrule.jpg`), or you can upload an image and then reach via a relative path (ex `http://localhost:8000/images/catrule.jpg`). 

## Frontends where?
ReactJS -> url coming
Android -> Coming soon
