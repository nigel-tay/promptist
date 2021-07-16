# Promptist
https://promptist.herokuapp.com/

## Description

A General Assembly Project

Promptist is a prompt generator for creatives seeking ideas for a new art project or something fun to create. Creatives may use the generated prompt to create art they may not have thought of themselves. It is also a collective platform for artists of all mediums to showcase their works based on that prompt.

### Technologies Used

- Django
- PSQL
- django-sass 1.0.1(SASS Compiler)
- django-bootstrap-icons (icons)
- Bootstrap4
- Cloudinary (https://cloudinary.com/documentation/cloudinary_get_started)
- Pillow

For deployment:
- Heroku
- White Noise 
- gunicorn
- dj_database_url (for easy grabbing of database details from Heroku)


### Wireframes
Visit the link below to view the wireframes in Figma:
https://www.figma.com/file/ZieVt7CHcL2Ro8g8EokCgs/Promptist?node-id=0%3A1
#### Initial planning on figma for layout and navigation ideation<br/>
Mobile Layout<br/>
<img src="images/mobilewire.png" width="70%"><br/>
Desktop Layout<br/>
<img src="images/desktopwire.png" width="70%">

### User Stories

User should be able to:
- Navigate to their intended destination with the given buttons/navigation options.
- Generate useful prompts that helps break through their artist block.
- Have the ability to register if they want to have access to upload and gallery functionality.
- Upload their artwork if they are logged in.
- Search to filter through the gallery/their uploaded works.



---

## Planning and Development Process

Phase 1: Pre-Project week<br/>
Finish up the layouts and planning of the database. Set-up the base of the frameworks used so that everything is ready to go by Monday.

Phase 2: First half of Project Week<br/>
Ensure that the app has solid unbreakable logic. Ensure that every page is accessible and common functions are working.

Phase 3: The final stretch; Finishing up the Project<br/>
Check for any bugs. Test and retest. Do some final touchups to the user experience of the app, as well as implement a desktop design for the application.

#### Final App<br/>
Desktop Layout:</br>
Landing Page</br>
<img src="images/landingpage.png" width="70%"></br></br>
Register Page:</br>
<img src="images/registerpage.png" width="70%"></br></br>
Login Page:</br>
<img src="images/loginpage.png" width="70%"></br></br>
Prompt Generator Page:</br>
<img src="images/generatorpage.png" width="70%"></br></br>
Showing generated prompt after Generate button is clicked</br>
<img src="images/generatorpage-generate.png" width="70%"></br></br>
Gallery Page; showing all user's uploaded artworks:</br>
<img src="images/gallerypage.png" width="70%"></br></br>
Profile Page; individual users can view their finished works here:</br>
<img src="images/profilepage.png" width="70%"></br></br>

Mobile Layouts:</br>
<img src="images/mobileprofile.png" width="70%">
<img src="images/mobilegallery.png" width="70%">
<img src="images/mobilegenerator.png" width="70%">
<img src="images/mobilelanding.png" width="70%">

### Problem-Solving Strategy

My main strategy to problem solving is to break down the task at hand into smaller bite sized pieces. By breaking it down, the problem can be solved through it's individual pieces and eventually the whole problem is solved. Also, ask those around you for help; growth is achieved by inquiring greater minds.

### Unsolved problems

- User are not able to edit the prompt once they upload an image. They would have to delete and reupload the same image if they want to change the prompt.
- I wanted to implement a typewrite animation for the prompt generator but was not able to, due to time constraints.

---
