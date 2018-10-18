# A Curious Cottage
#### A century-old riddle
For this project, I decided to combine my affection for games and novels. I am working on a little interactive short story set in an old, dusty cottage.

-  [Hypertext fiction](https://en.wikipedia.org/wiki/Hypertext_fiction)
-  [Gamebook](https://en.wikipedia.org/wiki/Gamebook)

    A gamebook is a work of printed fiction that allows the reader to participate in the story by making choices. 
    The narrative branches along various paths, typically through the use of numbered paragraphs or pages. 
    Gamebooks are sometimes called choose your own adventure books or CYOA after the influential Choose Your Own Adventure series 
    originally published by US company Bantam Books. Gamebooks influenced hypertext fiction.

## UX
 
- This website is for gamers, visual novel or choose-your-own story readers, mystery novels fans, people with 10 minutes to spare.
- User stories!!
- Wireframes: [main story]() and [leaderboard]().
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
    - The project uses **JQuery** to simplify DOM manipulation.
- [Python 3.6.5](https://www.python.org/)
    - Python is a clear and powerful object-oriented programming language, comparable to Perl, Ruby, Scheme, or Java.
- [Flask]()
    - Flask is a microframework for Python based on Werkzeug and Jinja 2.
- [Jinja2]()
    - Jinja2 is a full featured template engine for Python. 
     It has full unicode support, an optional integrated sandboxed execution environment, widely used and BSD licensed.
- [Html & CSS]()
    - Lorem.
## Testing
>In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.
Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.
For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

- Complexity of leaderboard's view
I have chosen push the complexity into my template, to allow for a simpler view.


> 1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.
You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.
If this section grows too long, you may want to split it off into a separate file and link to it from here.

<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>

## Deployment

This project has been deployed using Heroku.
#### [A Curious Cottage](https://ci-vero-practicalpython.herokuapp.com/)

- [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
    - The ‘Deploy to Heroku’ button enables users to deploy apps to Heroku without leaving the web browser, and with little or no configuration. The button is ideal for customers, open-source project maintainers or add-on providers who wish to provide their customers with a quick and easy way to deploy and configure a Heroku app.
The button is well-suited for use in README files, and is intended to serve as a replacement to a list of manual steps typically required to configure an app.



>This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).
In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
>- Different values for environment variables (Heroku Config Vars)?
>- Different configuration files?
>- Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.
## Credits
### Disclosure
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
- Most of pictures and patterns used in this site were all digitally drawn by Veronique Savard (nuagesdencre.com). They should not be used elsewhere.
Three of the drawings were directly inspired from the following:
    - [George Goodwin Kilburne's](https://en.wikipedia.org/wiki/George_Goodwin_Kilburne) [A Game of Chess](https://www.1st-art-gallery.com/George-Goodwin-Kilburne/A-Game-Of-Chess.html)
    - [The wedding of Wedding Margaretha Zelle and Rudolph MacLeod](https://www.friesmuseum.nl/en/collection/blog-mata-hari/dont-think-that-im-bad/)
    - This picture of [Vera Menchik](http://www.chesshistory.com/winter/pics/cn3433_menchik.jpg)
- The pattern used in the background was found on [Subtle Patterns]()
- The photographs displayed on the websites were found on Pexel.

    - [Cottage (or cabin)](https://www.pexels.com/photo/clouds-country-countryside-daylight-542382/)
### Acknowledgements
>- I received inspiration for this project from X