## **`peter`: Your Linux Command Translator (Peter Griffin Edition)**

![Banner](docs/assets/banner.png)

Hey Lois, ever wanted to understand those geeky Linux commands but were afraid you'd end up more confused than a monkey trying to do its taxes? Well, fear no more! `peter` is here to break down those brainy terminal things in a way even I can understand (well, mostly).

![Demo](docs/assets/demo.gif)

### **How the Heck Does This Work?**

1. **You type somethin' like:** `peter ls` or `peter "grep hello world.txt"`
2. **I whip out my trusty Gemini AI translator:** This thing's smarter than Stewie after a bowl of spinach, and it'll turn that boring command into a hilarious hot mess of an explanation.
3. **You laugh (or groan), but hey, at least you learn somethin':** Maybe you'll actually remember what those commands do instead of just blindly copying stuff from the internet like a parrot.

### **Gettin' Started (For Dummies Like Me)** <img src="docs/assets/apikey.png" alt="Whatever" width="250" align="right">

1. **Make sure you got that pip thing installed:** You know, for downloading packages and stuff.
2. **Use pip to install this amazingness:** 
    ``` bash
     $ pip install peter-explains
    ```
3. **Set the API Key:** Get one o those for free from [here](https://aistudio.google.com/app/). The run:
    ``` bash
     $ peter --api <YOUR_API_KEY> 
     $ peter --api <YOUR_CORRECT_API_KEY>
    ```
4. **Boom! Unleash the Peter:** Try something like `peter grep`. Just don't ask me to explain it – that's the AI's job.
5. **Too Slow?** I know. This thing can be slow at first. But try running the same command again. See that? That's the magic of cache.

> [!TIP] 
> Confused about what a fancy-ass command does? Put em inside `" "` after peter. I'll handle the rest.
> ``` bash
> $ peter "find . -name "node_modules" -type d -prune -exec rm -rf '{}' +"
> ```

> [!WARNING]
> ### Retep is gonna ruin your day if you try to use it without the API KEY
> 
>     Don't worry. Meg's here to help. You need a FREE Google Gemini API KEY.
> 
>     - Get yours from here: [https://aistudio.google.com/app/](https://aistudio.google.com/app/)
>     - Save the `API KEY` to your Environment by running the following:
> 
>       $ peter --api <YOUR_API_KEY> 

> [!TIP]
> If yo dumbass scews up setting the API key, run the following to delete and try setting it up again. 
> ``` bash
> $ peter --delete-api
> ```

### Help

Run the following for help. Probally won't help.
``` bash
  $ peter --help
```
Need more?

<p align="center">
    <a href="http://atick.dev/peter-explains/">
    <img src="docs/assets/docs.png" alt="Button description" width="400">
    </a>
</p>

### **For the Brainiacs (a.k.a. Potential Contributors)**

Hey Meg, turns out even _I_ can't make this thing perfect on my own. If you're the type who knows their way around Python and AI, feel free to poke around the code and make it even funnier (or, dare I say, _educational_).

``` bash
$ git clone https://github.com/atick-faisal/peter-explains
$ cd peter-explains
$ pip install -r requirements.txt
$ pip install -r requirements-dev.txt
$ pip install -e .
```

> [!NOTE]
> Make sure you test your crap before making a PR. I ain't got time for yo buggy code.
> You're gonna need the API key in your exvironment to run the tests.
> ```bash
> $ export GOOGLE_API_KEY=<YOUR_API_KEY>
> ```
> Run the tests like this:
> ```bash
> $ pytest
> ```
> Don't forget to check your linting before pushing:
> ```bash
> $ python -m pylint $(git ls-files '*.py') --rcfile .pylintrc
> ```



### **Disclaimer** <img src="docs/assets/meg.png" alt="Whatever" width="150" height="150" align="left">

I ain't responsible if this tool makes you dumber, offends your delicate sensibilities, or causes your computer to explode. Use at your own risk, and remember: laughter is the best medicine... unless you're choking on a hot dog. Then you probably need a doctor.

**Let me know if you want me to make it even more absurd or add specific installation instructions based on your project setup!**
