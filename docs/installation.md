## Installing Peter Explains Linux (For Dummies)

Alright folks, if you wanna get this hot mess of a tool onto your computer, pay attention. It shouldn't be harder than setting up a VCR (but then again, who even uses those anymore?).

![Demo](assets/installation.gif)

### Prerequisites

-   **Brain (Sort Of):** You don't need to be a genius to install this thing, but a basic understanding of computers is helpful. If you think a terminal is a bus station, you might wanna brush up on your skills first.
-   **Python (The Real Kind):** This tool ain't written in the language of snakes, it's made with Python. Make sure you have Python installed on your system. Don't know how to check? Google it, even Meg can figure that out.
-   **PIP (The Package Thingy):** PIP is what helps you install all sorts of fancy Python packages, and you'll need it to get this project workin'. Don't worry, it usually comes bundled with Python.

### Installation Steps

#### Option 1: Using pip (For Those Who Like Things Simple)

1. **Open Your Terminal:** This is the scary black box where you type stuff. If you ain't never used one before, good luck, you're gonna need it.
2. **Run This Magical Command:** Type the following, then hit Enter:

    ```bash
    pip install peter-explains
    ```

    This tells PIP to fetch the 'peter-explains' package and install it for ya. Ain't technology amazing?

!!! warning "Retep is gonna ruin your day if you try to use without the API KEY"

    Don't worry. Meg's here to help. You need a FREE Google Gemini API KEY

    - Get yours from here: [https://aistudio.google.com/app/](https://aistudio.google.com/app/)
    - Add the `API KEY` your Environment by running the following:

    ```bash
      export GOOGLE_API_KEY=YOUR_KEY
    ```

    - (Recommended) Add this line to your `.bashrc` or `.zshrc`

#### Option 2: From Source (For Masochists)

1. **Fork and Clone (GitHub Stuff):** If you're a glutton for punishment, head to GitHub, fork the repository for this project, and clone it. You'll need Git for this.
2. **Installin' Time:** Navigate to your cloned directory in your terminal, then run this:

    ```bash
    pip install .
    ```

### Test It Out (See If It Actually Works)

Now for the moment of truth. Type the following into your terminal:

```bash
peter --help
```

If you see a bunch of help text (and likely some insults from me), then congrats, you've installed it! If you get errors, well... maybe this thing ain't for you after all.

### Important Note for API Keys

Don't forget, you'll need a fancy-pants API key from wherever you're gettin' your LLM stuff. You'll need to set that up as an environment variable: [https://aistudio.google.com/app/](https://aistudio.google.com/app/) before this tool will really work. Don't come cryin' to me if you skip this part.

## Troubleshooting (When Things Go Wrong, As They Probably Will)

-   **"I Don't Get It..."** Don't worry, most of us don't. Read the README file (if it even exists). You might stumble upon the answer.
-   **"It's Still Broken!"** Did you try turning it off and on again? Okay, in all seriousness, try searching the GitHub issues on the project's page. Someone else probably messed up the same way you did.
-   **"I Found a Bug!"** Ugh, like a freakin' cockroach in the kitchen. Well, report it on GitHub, and maybe someone smarter than you can fix it (that shouldn't be hard to find).

    **That's it! If you made it this far, you're either a tech whiz or a glutton for punishment (or both). Now go learn some Linux commands the Peter Griffin way.**

Let me know if you want specific links for the GitHub repo or API key instructions woven into this guide!
