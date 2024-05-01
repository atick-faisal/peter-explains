## Peter Explains Linux: A Contribution Guide (For Those Who Ain't Scared)

Hey there, so you wanna help out with this Peter Explains Linux thing, huh? Well, good luck, you must be braver than Lois walkin' into the panty store. But hey, if you ain't afraid of a little work (and a lot of my insults), then this guide's for you.

**What We Do Here:**

This project takes the boring world of Linux commands and explains them in a way even Brian might understand... well, maybe. We use a fancy Large Language Model (LLM) – basically a computer that's better at talkin' than Stewie – to translate those cryptic commands into Peter Griffin-speak.

**How You Can Help:**

There's more to this than just Brian's stupid, existential ramblings. Here's how you can contribute:

-   **Bug Squashin':** Found a bug that makes this thing about as useful as a chocolate teapot? Report it! The more details you give, the faster we can get this thing workin' right (sorta).
-   **New Feature Frenzy:** Got an idea for a killer new feature? Spit it out! Whether it's explainin' more commands, addin' fancy options, or makin' the whole thing less confusing than Peter after a trip to Vegas, let us know.
-   **Code Wranglin':** Think you can write code better than Chris writes essays? We're always lookin' for improvements to the codebase. Just make sure your code ain't spaghetti like Brian's social life.
-   **Translation Time:** Wanna help Peter speak a different language? We're open to makin' this thing multilingual, so foreign folks can also enjoy Peter's unique perspective on Linux.

**Before You Dive In:**

-   **Read the Docs:** We got a whole bunch of [documentation](https://atick.dev/peter-explains/) to help you get started. Read it like you're studyin' for a test, and you'll be less lost than Meg at a family dinner.
-   **Get the API Key:** You need a fancy-pants API key from [here](https://aistudio.google.com/app/). You'll need to set that up as an environment variable before this tool will really work. Don't come cryin' to me if you skip this part.
    
    !!! important
        Make sure to save it to your Environment by running the following. You're gonna need it to run the tests.:
        ```bash
        $ export GOOGLE_API_KEY=<YOUR_API_KEY>
        ```

-   **Git Gud:** You better know how to use Git before you start messin' with the code. Unless you wanna end up like Cleveland after a night at the Drunken Clam, learn the basics.
-   **Python Power:** This whole thing is built on Python. So if you don't know Python from a peanut, you might wanna brush up on your skills first.
-   **Read the Code:** Don't come in here like a bull in a china shop. Take some time to understand how the code works before you start makin' changes.
-   **Test Your Stuff:** Nobody wants a buggy mess. Make sure your changes actually work before you submit them.

**How to Contribute:**

1. **Fork It!:** Head over to GitHub and fork this repository. Think of it like makin' your own copy of Peter's Family Guy script, but with less chicken fights.
2. **Branch Out:** Create a new branch for your changes. This keeps things organized and prevents you from steppin' on other people's work (like Meg steppin' on Peter's patience).
3. **Code Away!:** Make your changes, write clear comments (even a monkey like Brian could understand!), and test everything thoroughly.
4. *Test the Hell out of it!:* Make sure your changes actually work before you submit them. We don't want a buggy mess.

    !!! tip
        Theres tests in the `tests` directory. Run them to make sure your changes don't break anything.
        ```bash
        $ pytest
        ```
        You wanna see something like this:
        ```
        =========== test session starts ==========
        platform linux -- Python 3.10.12, pytest-8.2.0, pluggy-1.5.0
        rootdir: /mnt/Data/Cloud/Python/peter-explains
        plugins: cov-5.0.0, console-scripts-1.4.1
        collected 7 items                

        tests/peter_explains/test_peter.py .......  [100%]

        =========== 7 passed in 17.51s ===========
        ```

5. **Push It Good:** Push your changes to your forked repository. This is like showin' off your work to the class.

    !!! tip
        You might wanna check yo linting before you push. Run the following to check for any linting errors:
        ```bash
        $ python -m pylint python -m pylint $(git ls-files '*.py') --rcfile .pylintrc
        ```
        It better be a 10.0/10.0 like Peter's IQ.
        ```
        Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
        ```

6. **Pull Request Time:** Open a pull request to this repository. This is basically sayin', "Hey, check out my awesome changes!"
7. **Review and Repeat:** We'll review your pull request and give you feedback. Be prepared for some back-and-forth, just like Peter and Lois bickerin' about the bills. But don't worry, we ain't gonna be as harsh as Stewie.

**Important Stuff (Don't Skip This Part):**

-   **Be Respectful:** Even though this is Peter Explains Linux, we still expect everyone to be respectful of each other. No name-callin', like Peter callin' Quagmire a pervert (even though it's true).
-   **Follow the Code Style:** We have a certain way we like our code to look. Follow the style guide so your code doesn't stick out like a sore thumb (like Peter in a speedo).
-   **Licensing:** All contributions to this project are licensed under the MIT License. Basically, you're giving us permission to use your code, and we're doin' the same for you (with proper credit, of course).

**So, You Think You Can Hack It?**

If you think you can handle the pressure (and the occasional Peter-ism), then we welcome your contributions! Just remember, with great power comes great responsibility (and the possibility of gettin' a wedgie from Lois).

Good luck, and don't screw it up!

---
