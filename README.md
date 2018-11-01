# [A Curious Cottage](https://ci-vero-practicalpython.herokuapp.com/)
#### A century-old riddle
For this third milestone project, I decided to combine my affection for games and novels. I am working on a little interactive short story set in an old, dusty cottage.

- This website is for gamers, visual novel or choose-your-own story readers, mystery novels fans, people with 10 minutes to spare.

-  [Hypertext fiction](https://en.wikipedia.org/wiki/Hypertext_fiction)
-  [Gamebook](https://en.wikipedia.org/wiki/Gamebook)

    A gamebook is a work of printed fiction that allows the reader to participate in the story by making choices. 
    The narrative branches along various paths, typically through the use of numbered paragraphs or pages. 
    Gamebooks are sometimes called choose your own adventure books or CYOA after the influential Choose Your Own Adventure series 
    originally published by US company Bantam Books. Gamebooks influenced hypertext fiction.

## UX
 ![](./static/stories/USERS_STORIES.jpg?raw=true)
 
| User    | Purpose of visit (User type: Visitor)                                                                                                                                                                                 | What the user wants                                                                                                                                                                                                                                                                                                                                                                                       | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :------ | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Camille | Camille has a huge collection of gaming apps on her phone and she likes games that are not too long but keep her entertained. Camille likes to personalize her gaming experience through avatars or funny usernames. | As a site visitor, Camille wants to play a game that offers personalization. Camille also wants to learn more about the rules and the type of game she is playing. | Camille plays the game at the same time as her best friend, while they wait on their coffees. Camille has a lot of fun deciding on her favourite colour and her spirit animal. She is pleased to see her details in the story’s first page. She reads through the pages quickly and fails to answer the riddle. Her details are in the leaderboard however and she is happy nonetheless with her experience. She looks at the ‘About’ page to learn more about gamebooks.   |
| Harry   | Harry and his son enjoy games of wit and challenging each other. They tend to look up things on the internet together to learn more about the subjects they encounter.| As a visitor, Harry wants to be able to solve the riddle presented in the game according to the hints and instructions give. Harry also expects that the game is ad-free, that there is no subscription or payment needed at least for a first experience. Harry likes to know he can reach the webmaster if he has any comments to make.                                                                                                                                                                           | Together with his son, Harry picks a username, a favourite colour and a spirit animal. He reads the story out loud and discuss possible answers to the riddle with his son. Harry’s wife gets involved as she quite enjoys the story. After a few incorrect attempts (mainly due to typos), Harry gets the answer right. He sends a message to the webmaster through the contact form to share his impressions. |
| Mike    | Mike like to play games to offer puzzles and riddles. He enjoys pretending to be a detective.                                                                                                                   | As a site visitor, Mike wants to be able to play a game that offers various outcomes depending on his choices.  Mike also wants to see his progression in the game and measure his accomplishments against his friends’ results.                                                                                                                                                                               | Mike is introduced to ‘A Curious Cottage’ game by his girlfriend, who knows he likes puzzles. She managed to solve the riddle and shows him her entry in the leaderboard. Mike wants to do the same. He reads the story and spots a hint in one of the collapsible paragraphs. He is able to answer the riddle faster than his girlfriend, according to the time displayed on the leaderboard.|
| Lou     | When Lou is not entertaining his daughters with cute videos and websites, he likes to read using the family iPad.| As a site visitor, Lou wants to play a game that is relaxing and requires his concentration. Lou wants to use the iPad to play the game online through a website since the app on the iPad are mainly for the girls. | Lou is able to access the website without having to download anything. The story interests him and he reviews all possible options to solve the riddle offered. Lou looks at every picture carefully and enters ‘chessboard’ as an answer. When he notices the error message saying the answer has two words, Lou is able to answer correctly.                                                                                                                                                                                                                                                                                                  |


* Main story [wireframe](./planning/dashboard.png)
* Leaderboard [wireframe](./planning/leaderboard.png)



 ## Features
> In this section, you should go over the different parts of your project, and describe each in a sentence or so.
- Original story surrounding the riddle to solve
- Responsive design
- Dynamic Leaderboard
- Contact form
 
## Functionality
- Story elements of the website 
    - Inspired by the concept of [Interactive fiction](https://en.wikipedia.org/wiki/Interactive_fiction) 
    - This is a short mystery story where the readers have to become pseudo-investigators. 
    The readers are invited from their arrival on the home page to provide information and start reading the gamebook.
    A riddle is given to the readers and their assistance is requested. Throughout the pages, the readers can reveal 
    more aspects of the story by exploring 
    the different options available via buttons. The story details lead the readers to solve the riddle. 
- Game Information 
   - Rules 
        - The readers can review the guidelines of the experience proposed by the website. 
   - Leaderboard 
        - The readers can review their progress (i.e. time they started reading, status of the riddle, information they provided) 
        via the leaderboard. This information is updated as the readers visit the web app and even when they let another person read the story on a same device.
- About 
    - The page provides information about the game concept itself and the inspiration behind the 'point and click' exploration of a story.
    - Contact form 
        - This allows the readers to reach out to the webmaster and give their comments.

## Technologies Used
> In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.
- [JQuery](https://jquery.com)
    - The project uses JQuery to simplify DOM manipulation. jQuery is a JavaScript library that was created to make it easier and simpler to write JavaScript and HTML.
    
- [Python 3.6.5](https://www.python.org/)
    - Python is a clear and powerful object-oriented programming language, comparable to Perl, Ruby, Scheme, or Java.
- [Flask]()
    - Flask is a microframework for Python based on Werkzeug and Jinja 2. This project uses Flask to structure the website and offer a better user experience.
- [Jinja2]()
    - Jinja2 is a full featured template engine for Python. 
     It has full unicode support, an optional integrated sandboxed execution environment, widely used and BSD licensed.
- [CSS](https://simple.wikipedia.org/wiki/Cascading_Style_Sheets)
    - Cascading Style Sheets, or CSS, are a way to change the look of HTML and XHTML web pages. CSS was designed by the W3C, and is supported well by most modern web browsers. The current version of CSS is CSS3. CSS4 is available, but is split into parts.
- [HTML](https://simple.wikipedia.org/wiki/HTML)
    - HyperText Markup Language (HTML) is a markup language[1] for creating a webpage. Webpages are usually viewed in a web browser. They can include writing, links, pictures, and even sound and video. HTML is used to mark and describe each of these kinds of content so the web browser can display them correctly. HTML can also be used to add meta information to a webpage.

I used Git & GitHub for version control. Each new piece of functionality should be in a separate commit.
I used branches for major changes, features and enhancement elements.

## Testing

#### Javascript, CSS & HTML Validation

- [CSS Validation Service](http://jigsaw.w3.org/css-validator/)
I ensured my CSS had no typos, errors or incorrect uses using The CSS Validation service.
<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>

- [JSHINT](https://jshint.com/about/)
I used JSHINT to pinpoint any bug or typo in my scripts.

- [Nu Html Checker](https://validator.w3.org/nu/about.html)
I used the Nu checker to catch unintended mistakes in my Html documents.

- Responsiveness and browser compatibility
[Browserling](www.browserling.com/)
This website has been tested on multiple devices and browsers to ensure utmost responsiveness.
I have also used the website 'Browserling' for that purpose.
The only major change to the user interface is the navigation bar, which contains icons for smaller viewports such as 
phones, instead of the name of the pages presented on bigger viewports. This change is deliberate to offer a better user experience.


> 1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.
You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.
If this section grows too long, you may want to split it off into a separate file and link to it from here.


- Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

## Hurdles
You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

- Complexity of leaderboard's view
I have chosen push the complexity into my template, to allow for a simpler view.
## Deployment
This project has been deployed using Heroku.

- I realised the website using [PyCharm](https://www.jetbrains.com/pycharm/), which is a Python IDE. The app was tested in a development environment with a debugging option.
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
### Acknowledgements

 I thank my friends and family who have taken time to play the game and give me feedback.
 A huge thank you to my mentor for constructive criticism and an eagle eye for any typo and/or weak code.
 