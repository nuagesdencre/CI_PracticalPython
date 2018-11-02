# [A Curious Cottage](https://ci-vero-practicalpython.herokuapp.com/)
#### A century-old riddle
For this third milestone project, I decided to combine my affection for games, mystery and novels. 
Enjoy this interactive short story set in an old, dusty cottage. 

#### This website is for bookworms, gamers, visual novel or choose-your-own story readers, mystery novels fans, people with 10 minutes to spare.

- This is a short mystery story where the readers have to become pseudo-investigators (and pseudo-gardeners). 
    The readers are invited from their arrival on the home page to provide their details to personalize their experience through the gamebook.
    A riddle is given to the readers under the premise that, as protagonists of the story, their investigative talents are requested. Throughout the pages, the readers can reveal 
    more aspects of the story by exploring 
    the different options available via buttons and collapsible paragraphs. Skipping some means missing out on various hints and historical tidbits. The exploration of the cottage through the story added to the curiosity of the readers will allow them to solve the riddle.

## UX
 
 ### User stories
 [Meet our Users!](./static/stories/USERS_STORIES.jpg?raw=true)
 
| User    | Purpose of visit                                                                                                                                                                                  | What the user wants                                                                                                                                                                                                                                                                                                                                                                                       | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :------ | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Camille | Camille has a huge collection of gaming apps on her phone and she likes games that are not too long but keep her entertained. Camille likes to personalize her gaming experience through avatars or funny usernames. | As a site visitor, Camille wants to play a game that offers personalization. Camille also wants to learn more about the rules and the type of game she is playing. | Camille plays the game at the same time as her best friend, while they wait on their coffees. Camille has a lot of fun deciding on her favourite colour and her spirit animal. She is pleased to see her details in the story’s first page. She reads through the pages quickly and fails to answer the riddle. Her details are in the leaderboard however and she is happy nonetheless with her experience. She looks at the ‘About’ page to learn more about gamebooks.   |
| Harry   | Harry and his son enjoy games of wit and challenging each other. They tend to look up things on the internet together to learn more about the subjects they encounter.| As a visitor, Harry wants to be able to solve the riddle presented in the game according to the hints and instructions give. Harry also expects that the game is ad-free, that there is no subscription or payment needed at least for a first experience. Harry likes to know he can reach the webmaster if he has any comments to make.                                                                                                                                                                           | Together with his son, Harry picks a username, a favourite colour and a spirit animal. He reads the story out loud and discuss possible answers to the riddle with his son. Harry’s wife gets involved as she quite enjoys the story. After a few incorrect attempts (mainly due to typos), Harry gets the answer right. He sends a message to the webmaster through the contact form to share his impressions. |
| Mike    | Mike like to play games to offer puzzles and riddles. He enjoys pretending to be a detective.                                                                                                                   | As a site visitor, Mike wants to be able to play a game that offers various outcomes depending on his choices.  Mike also wants to see his progression in the game and measure his accomplishments against his friends’ results.                                                                                                                                                                               | Mike is introduced to ‘A Curious Cottage’ game by his girlfriend, who knows he likes puzzles. She managed to solve the riddle and shows him her entry in the leaderboard. Mike wants to do the same. He reads the story and spots a hint in one of the collapsible paragraphs. He is able to answer the riddle faster than his girlfriend, according to the time displayed on the leaderboard.|
| Lou     | When Lou is not entertaining his daughters with cute videos and websites, he likes to read using the family iPad.| As a site visitor, Lou wants to play a game that is relaxing and requires his concentration. Lou wants to use the iPad to play the game online through a website since the app on the iPad are mainly for the girls. | Lou is able to access the website without having to download anything. The story interests him and he reviews all possible options to solve the riddle offered. Lou looks at every picture carefully and enters ‘chessboard’ as an answer. When he notices the error message saying the answer has two words, Lou is able to answer correctly.                                                                                                                                                                                                                                                                                                  |


* Main story [wireframe](./planning/wireframe.png)
* Leaderboard [wireframe](./planning/leaderboard.png)



 ## Features

- Responsive design
    - This website can be viewed on devices big or small without any impact on content or user experience.
 
- An original story where the reader needs to solve a mysterious riddle
    - From the landing page, the readers are invited to introduce themselves and investigate an old cottage. 
    Additional paragraphs are available for a more thorough exploration of the house and hints relevant to the riddle. 
    The readers can click through and provide their answer on the epilogue page.    
- Game Information 
   - Rules 
        - The readers can review the guidelines of the experience proposed by the website. 
   - Dynamic Leaderboard 
        - The readers can review their progress (i.e. time they started reading, status of the riddle, information they provided) 
        via the leaderboard. This information is updated as the readers visit the web app and even when they let another person read the story on a same device.
- About 
    - The page provides information about the game concept itself and the inspiration behind the 'point and click' exploration of a story.
    - Contact form 
        - This allows the readers to reach out to the webmaster and give their comments.

## Technologies Used
- [JQuery](https://jquery.com)
    -  jQuery is a JavaScript library that was created to make it easier and simpler to write JavaScript and HTML.
    The current project uses JQuery to simplify DOM manipulation.
- [Python 3.6.5](https://www.python.org/)
    - Python is a clear and powerful object-oriented programming language, comparable to Perl, Ruby, Scheme, or Java. Most of this project's elements and the game logic is built using python via Jinja2.
- [Flask]()
    - Flask is a microframework for Python based on Werkzeug and Jinja 2. This project uses Flask to structure the website and offer a better user experience.
- [Jinja2]()
    - Jinja2 is a full featured template engine for Python. 
     It has full unicode support, an optional integrated sandboxed execution environment, widely used and BSD licensed. This was used for the game logic and the dynamic elements of the website, along with the forms management.
- [CSS](https://simple.wikipedia.org/wiki/Cascading_Style_Sheets)
    - Cascading Style Sheets, or CSS, are a way to change the look of HTML and XHTML web pages. 
    CSS was used in this project for the user interface and overall website look - button sizing, background image, etc.
- [HTML](https://simple.wikipedia.org/wiki/HTML)
    - HyperText Markup Language (HTML) is a markup language for creating a webpage.  They can include writing, links, pictures, and even sound and video. HTML is used to mark and describe each of these kinds of content so the web browser can display them correctly.
    HTML was essential to this project as it builds up the views and DOM elements of the web app, structured by Flask.
    
- [EmailJS](https://www.emailjs.com/)

    A Javascript library using client-side code to connect to supported email services. I used this service to generate the contact form template and connect to my existing Gmail account.

I used Git & GitHub for version control. Each new piece of functionality should be in a separate commit.
I used branches for major changes, features and enhancement elements.

## Testing

1. Responsiveness and browser compatibility

    - [Browserling](www.browserling.com/)
    
        This website has been tested on multiple devices and browsers to ensure utmost responsiveness.
        I have also used the website 'Browserling' for that purpose.
    
    The navigation bar changes from small to big viewports. It displays icons for smaller viewports such as 
    phones, instead of the full name of the pages visible on bigger viewports. This change is deliberate to offer a better user experience.

2. Index/Home page

    I. Upon my first visit, a welcome message displays "...whoever you are!" and a button shows the message "Come along please".
    
    II. Links are easily identified through the usage of button elements or underline upon hovering. For instance, the links within the navigation bar change color when the mouse hovers them and a squiggly underline appears upon mouse/finger presence.
    
    III. Upon a second visit at the home page, once I have submitted details for a first playthrough, the welcome message displays the name I inputted and two choices are offered below: a link to continue to play or a button to press if I am someone new to the game.
    Clicking the link brings me back to the story's introduction, showing the details I provided. Choosing the button makes me drop my current session. I am then redirected to the index page with the welcome message displaying "...whoever you are!".

3. Play page
    
    I. When I try to submit an empty form, an error message about the required fields appears.
    
    II. When I type in a single letter to rush to the next step, an error message inviting me to provide the minimum amount of characters per field appears.
    
    III. When I input data using all capitals letters, the game session stores the colour input and animal input in lower case. They are displayed accordingly in the leaderboard and first part of the story.
    
4. Story section

    - Introduction
    
        I. The inputted data gathered on the Play page is displayed on the Introduction page. If data has not been provided yet, I am redirected to the Play page.

        II. I can use the back arrow or the navigation bar to check other pages without error messages. I can return to the introduction page via the Game Info page or the Home page.
        
        III. Once I click the submit button, the "game start" timestamp is stored in the session.
        
    - Pages 1, 2, 3
        
        I. Using the back arrow or backspace brings the following message "Confirm form submission" as moving along the story, I submit forms and store details in the session accordingly.
        This discourages me to go back to the previous page and to try and read carefully before clicking on a button.
        
        II. I can review the riddle given at the beginning of the story at the bottom of all pages. 
        This option has a different button colour and is separated clearly from the other exploration options.
        
        III. The exploration options are preceded on every page by "What do you do next?" to ensure I am aware that the steps forward are up to me.
        
        IV. When an option is toggled, the button colour changes. Its associated collapsible paragraph is surrounded by a border for clarity. By clicking on the same button, the paragraph can be hidden again.

    - Epilogue
    
        I. If I submit a correct answer, the input field disappears. I obtain the "Spot on" success message along with a short paragraph. There is an invitation to the leaderboard at the bottom of the page.The riddle status stored in session is "Solved".
        
        II. If I submit an empty field, the attempt number increases and I get the "Not quite" failure message. There is a short paragraph and an invitation to start over. The riddle status stored in session is "Unsolved".
        
        II. If I submit an incorrect answer, the attempt number increases and I get the "Not quite" failure message. There is a short paragraph and an invitation to start over. The riddle status stored in session is "Unsolved".
               
        IV. When I submit an answer, the "game end" timestamp is stored in session.

5. Game Info page

    I. There are two buttons at the top of the page: one leads to the story's introduction if details have been inputted already, other to the play page; the other guides me to the Leaderboard.
    
    II. The rules of the game are listed under the buttons.
    
6. Leaderboard

    I. If I have not inputted any details yet, when I access the leaderboard, an alert prompting me to being the story and introduce myself pops up.
    
    II. If I have not yet inputted any details, when I access the leaderboard, the first entry contains default values and no timestamps recorded. 
    
    III. There can only be 4 entries (including the current reader's entry) displayed on the leaderboard at a time.
    
    IV. When I have inputted my details, the top entry on the leaderboard is highlighted and the provided details are displayed.
    They can change according to my progress in the story (i.e. have I submitted an answer, have I even started reading the story past the introduction).
    
    V. If I drop my session using the button available on the home/index view, my current details will be pushed into the existing data. The topmost entry will be defaulted again and the previous inputted data will be displayed in the entry below.
    Should there be many sessions dropped one after the other, only the 3 most recent records will be displayed, irrespective of the topmost entry.
    
    VI. The riddle status element of the leaderboard is highlighted if the value is "Solved" for a better user experience.
    
    - Leaderboard.py
    
        I. I have enclosed my default entry values into the Leaderboard object. When I create an instance (game_leaderboard), the data is assigned accordingly.
        
        II. I use two instance methods: get_leaders() to selects first 3 dictionary entries as per the data list index, and add_player() to record the current visitor's inputted details to data.
        The instance methods have been manually tested.
     
7. About page

    I. A quick explanation of the game is offered, along with musical suggestions. I can learn a bit more about gamebooks. There is a reminder relevant to where I can access the story.
    
    - Contact form:
        
         I.Placeholders are in the input field to offer guidance as of how to fill them.
         
         II. When I submit an empty form, an error message about the required fields appears.
            
         III. When I submit a form with incomplete information, which does not match the minimum character count of the field or the email format, an error message reminds me of the requirements.
            
         IV. When I submit the contact form with all inputs valid and requirements satisfied, an alert advising "The message has been sent!" pops on the screen. 
         An auto-reply message is issued to the email address I provided. As the webmaster, I receive the inputted information via EmailJS.

#### Python and Flask
   I ran the app in development mode by setting the FLASK_ENV=development environment variable in my evironment file.
   I used the [Werkzeug Javascript's in-browser debugger](http://werkzeug.pocoo.org/) at length during this project and tackled the bugs them one by one.
   It was most useful especially when I worked on the final page template.
   
   PyCharm was a wonderful tool to keep track of indentation and typos as well.

#### Javascript, CSS & HTML Validation

To the best of my ability, I conducted and documented tests to ensure that all of my website's functionality work well, while taking in account the user stories.

- [CSS Validation Service](http://jigsaw.w3.org/css-validator/)

    - I ensured my CSS had no typos, errors or incorrect uses using The CSS Validation service.
    - I made sure all DOM elements were readable and easily accessible (i.e. no small links or buttons) on all viewports.

- [JSHINT](https://jshint.com/about/)
    
    - I used JSHINT to pinpoint any bug or typo in my scripts.

- [Nu Html Checker](https://validator.w3.org/nu/about.html)

    - I used the Nu checker to catch unintended mistakes in my Html documents.      

## Hurdles

- Writing the story (the backbone of this project)
    
    I had to evaluate the length and complexity of the riddle to write an appropriate story. This turned out to be quite an exercise. I was lucky to receive input from friends and family members in that regard. This was a creative challenge that I hope I was able to deliver correctly.

- Complexity of leaderboard's view

    I had trouble determining the best way to display the current user information. I have chosen push the complexity into my template, to allow for a simpler view. 
    Setting up the leaderboard logic took me a little while but thanks to good advice, I ended up using a class and appropriated instance methods.

## Deployment
This project has been deployed using Heroku.

- I realised the website using [PyCharm](https://www.jetbrains.com/pycharm/), which is a Python IDE. The app was tested in a development environment with a debugging option.
Due to the limited scope of this project, the secret key was randomised and left into the app.py file.
- I prepared the Heroku required documents (Procfile and requirements.txt) according to the guidelines provided on Heroku [(link here)](https://devcenter.heroku.com/articles/deploying-python).
These documents indicate the language of the app to be deployed, along with its dependencies. I changed the app environment to production and removed the debugging option.

- I then logged in my Heroku account and created an app (ci-vero-practicalpython). A Heroku-hosted remote that’s associated with my app was created at the same time (https://git.heroku.com/ci-vero-practicalpython.git).
- On my PyCharm terminal, I provided my Heroku credentials, logged in and linked my existing github repository to the associated git remote hosted by Heroku.
- I used the "git push heroku master" to bring my project into the Heroku remote git repository.
- I entered the IP and PORT into the Heroku Config Vars fields (0.0.0.0 and 5000).
- Once done, I opened the app to ensure everything was working properly.

- This project can be deployed again using the below button.

  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
    
    This option is available since I provide an app.json file as per the guidelines found [here](https://devcenter.heroku.com/articles/heroku-button).

## Credits
### Disclosure and Coding References
- I learned a lot about Flask, Flask sessions and cookie-based sessions during this projects. These resources have been very useful and inspiring.
    - [Flask Sessions](http://flask.pocoo.org/docs/1.0/quickstart/#sessions)
    - [An Introduction to Sessions in Flask](https://www.youtube.com/watch?v=T1ZVyY1LWOg)
    - [Flask – Sessions](https://www.tutorialspoint.com/flask/flask_sessions.htm)
    - [How Secure Is The Flask User Session?](https://blog.miguelgrinberg.com/post/how-secure-is-the-flask-user-session)
    - [Reddit r/flask](https://www.reddit.com/r/flask/)
    - StackOverflow [Flask Frequent Questions](https://stackoverflow.com/questions/tagged/flask?sort=frequent&pageSize=15)

- The idea to turn a riddle game into a 'mystery-novella' came from various publications. Here are some helpful definitions I referred to.
    -  [Hypertext fiction](https://en.wikipedia.org/wiki/Hypertext_fiction)
    - [Interactive fiction](https://en.wikipedia.org/wiki/Interactive_fiction)
    -  [Gamebook](https://en.wikipedia.org/wiki/Gamebook)
    
        A gamebook is a work of printed fiction that allows the reader to participate in the story by making choices. 
        The narrative branches along various paths, typically through the use of numbered paragraphs or pages. 
        Gamebooks are sometimes called choose your own adventure books or CYOA after the influential Choose Your Own Adventure series 
        originally published by US company Bantam Books. Gamebooks influenced hypertext fiction.


### Content
- Information about 
FIDE - World Chess Federation: [(Source)](https://www.chess.com/article/view/fide-world-chess-federation-), [(Source)](https://www.fide.com/fide.html)
- The general information about Victorian households: [(Source)](http://starcraftcustombuilders.com/Architectural.Styles.VictorianKitchen.htm), [(Source)](http://www.victorian-era.org/victorian-era-last-names2.html)
- Private Investigator trivia: [(Source)](http://www.thrillingdetective.com/trivia/triv289.html)
- Information about Vera Menchik:
    - [(Review: Vera Menchik: A biography of the First Women’s World Chess Champion, with 350 games, By Robert B. Tanner)](http://georgiachessnews.com/2016/11/01/review-vera-menchik-a-biography-of-the-first-womens-world-chess-champion-with-350-games-by-robert-b-tanner/)
     - [(FIDE)](https://www.fide.com/fide.html) 
     - [(Mir Sultan Khan vs Vera Menchik Game)](http://www.chessgames.com/perl/chessgame?gid=1258409)
     - [(Wiki Page)](https://en.wikipedia.org/wiki/Vera_Menchik)
     - [(Internet Archive Wayback Machine)](https://web.archive.org/web/20091028034414/http://www.geocities.com/siliconvalley/lab/7378/menchik.htm)
### Media
- Most pictures and patterns used in this site were all digitally drawn by myself (credits to nuagesdencre.com). They should not be used elsewhere.
Three of the drawings were directly inspired from the following:
    - [George Goodwin Kilburne's](https://en.wikipedia.org/wiki/George_Goodwin_Kilburne) [A Game of Chess](https://www.1st-art-gallery.com/George-Goodwin-Kilburne/A-Game-Of-Chess.html)
    - [The wedding of Wedding Margaretha Zelle and Rudolph MacLeod](https://www.friesmuseum.nl/en/collection/blog-mata-hari/dont-think-that-im-bad/)
    - This picture of [Vera Menchik](http://www.chesshistory.com/winter/pics/cn3433_menchik.jpg)
- The pattern used in the background was found on [Subtle Patterns]()
- The photograph displayed on the website was found on Pexel.

    - [Cottage (or cabin)](https://www.pexels.com/photo/clouds-country-countryside-daylight-542382/)
## Acknowledgements

I thank my friends and family who have taken time to play the game and give me feedback.
 A huge thank you to my mentor for constructive criticism and an eagle eye for any typo and/or weak code.
 #### Thank you!
 ###
 
Feel free to get in touch if you have any comments or questions.

vero@nuagesdencre.com