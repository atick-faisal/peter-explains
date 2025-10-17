import random


class LoadingMessage:
    """
    Enhanced loading messages with more Peter Griffin personality and variety.
    """

    MESSAGES = [
        "Hang on, Lois, I'm tryin' to think here. This is harder than figuring out what's goin' on in Stewie's head.",
        "Jeez, this computer's slower than Quagmire after a night at The Clam.",
        "Ugh, I swear this thing gets dumber every day. It's like talkin' to Brian...",
        "Hold your horses! I'm workin' on it... kinda.",
        "Aw jeez, is this thing even plugged in? Meg wouldn't know the difference.",
        "C'mon, you pile of junk! I bet even Chris could figure this out faster...",
        "Alright, alright, I'm thinkin'... Thinkin' about how much better a cold beer would be right now.",
        "This is takin' longer than waitin' in line at the DMV. And that place smells better.",
        "Hey, if I don't figure this out soon, the freakin' TV guide's gonna be outdated.",
        "Loading... Loading... Nyehehehe! Just like that time I tried to use a computer!",
        "Searching the interwebs... or whatever you nerds call it.",
        "Consulting my vast knowledge of... uh... stuff and things.",
        "Asking Stewie for help... he's probably busy plotting world domination.",
        "Checking if this is one of those commands that actually does something useful.",
        "Reading the manual... just kidding, who reads manuals?",
        "Trying to remember what Brian taught me about computers... drawing a blank.",
        "Processing... like a really slow microwave that doesn't even heat food.",
        "Thinking really hard... you can almost hear the gears grinding.",
        "Consulting the ancient scrolls of Linux wisdom... or Google. Probably Google.",
        "Attempting to use my brain... this might take a while.",
    ]

    # Themed message categories for variety
    TV_REFERENCES = [
        "This is taking longer than a commercial break during my favorite show.",
        "Loading faster than channel surfing during football season.",
        "Processing like my old VHS player - slow and probably gonna break.",
        "Buffering worse than my streaming service during dinner time.",
    ]

    FOOD_REFERENCES = [
        "Cooking up an explanation... hope it's better than Lois's meatloaf.",
        "Brewing knowledge like a fresh cup of Pawtucket Patriot Ale.",
        "Mixing ingredients for the perfect command explanation recipe.",
        "Slow cooking this response... good things take time, right?",
    ]

    FAMILY_REFERENCES = [
        "Explaining this slower than Chris explains his homework.",
        "Taking longer than Meg takes to get ready for... anything.",
        "Processing at Stewie's genius level... okay, maybe not that fast.",
        "Working harder than Brian on his novel... that he'll never finish.",
    ]

    @staticmethod
    def get_random_message() -> str:
        """
        Returns a random message from all available message pools.

        Returns:
            str: A random loading message.
        """
        all_messages = (
            LoadingMessage.MESSAGES +
            LoadingMessage.TV_REFERENCES +
            LoadingMessage.FOOD_REFERENCES +
            LoadingMessage.FAMILY_REFERENCES
        )
        return random.choice(all_messages)

    @staticmethod
    def get_themed_message(theme: str = "random") -> str:
        """
        Get a message from a specific theme category.

        Args:
            theme: One of 'tv', 'food', 'family', 'general', or 'random'

        Returns:
            str: A themed loading message
        """
        theme_map = {
            "tv": LoadingMessage.TV_REFERENCES,
            "food": LoadingMessage.FOOD_REFERENCES,
            "family": LoadingMessage.FAMILY_REFERENCES,
            "general": LoadingMessage.MESSAGES,
            "random": LoadingMessage.MESSAGES + LoadingMessage.TV_REFERENCES +
                      LoadingMessage.FOOD_REFERENCES + LoadingMessage.FAMILY_REFERENCES
        }

        messages = theme_map.get(theme, LoadingMessage.MESSAGES)
        return random.choice(messages)


class ErrorMessage:
    """
    Enhanced error messages with more personality and helpful context.
    """

    MESSAGES = [
        "Aw crap, somethin' broke. Typical. Maybe Meg stepped on the keyboard again.",
        "Hey, if this thing gives ya the wrong answer, don't blame me. I'm just the idiot typin' stuff in.",
        "Alright, this might take longer than I thought. You got any beer in the fridge?",
        "Ugh, somethin' ain't right. Maybe I shoulda paid more attention to that computer class in high school.",
        "Aw jeez, I think I broke it. Don't tell Lois, she'll make me fix it.",
        "I swear, this thing's got more bugs than the Griffin house. And that's sayin' somethin'.",
        "Well, this is embarrassing. Even Cleveland could probably fix this.",
        "Error? What error? I don't see any... oh wait, there it is. Crap.",
        "Houston, we have a problem. And by Houston, I mean you, and by problem, I mean I screwed up.",
        "This is why I stick to watching TV. Computers are stupid.",
    ]

    # Categorized error messages for different contexts
    NETWORK_ERRORS = [
        "Internet's acting up again. Probably Quagmire downloading... stuff.",
        "Network error! The tubes are clogged or something.",
        "Connection problems. Did someone forget to pay the internet bill?",
        "Can't reach the servers. They're probably on vacation in the Bahamas.",
    ]

    API_ERRORS = [
        "API's having a moment. Like me when I see a sale at the beer store.",
        "Service is down. Probably getting a sandwich or something.",
        "The robots are on strike. This is how it starts, people!",
        "API key issues. Did you remember to feed it this morning?",
    ]

    USER_ERRORS = [
        "Command not found. Did you spell it right? I can barely spell my own name.",
        "Invalid input. Even I know that's not how you type things.",
        "User error detected. Don't worry, happens to the best of us. And the worst of us.",
        "Syntax error. It's like grammar, but for nerds.",
    ]

    @staticmethod
    def get_random_message() -> str:
        """
        Returns a random error message from all available categories.

        Returns:
            str: A random error message.
        """
        all_messages = (
            ErrorMessage.MESSAGES +
            ErrorMessage.NETWORK_ERRORS +
            ErrorMessage.API_ERRORS +
            ErrorMessage.USER_ERRORS
        )
        return random.choice(all_messages)

    @staticmethod
    def get_contextual_message(error_type: str = "general") -> str:
        """
        Get an error message appropriate for the context.

        Args:
            error_type: One of 'network', 'api', 'user', 'general', or 'random'

        Returns:
            str: A contextual error message
        """
        error_map = {
            "network": ErrorMessage.NETWORK_ERRORS,
            "api": ErrorMessage.API_ERRORS,
            "user": ErrorMessage.USER_ERRORS,
            "general": ErrorMessage.MESSAGES,
            "random": ErrorMessage.MESSAGES + ErrorMessage.NETWORK_ERRORS +
                      ErrorMessage.API_ERRORS + ErrorMessage.USER_ERRORS
        }

        messages = error_map.get(error_type, ErrorMessage.MESSAGES)
        return random.choice(messages)


class SuccessMessage:
    """
    Success messages to celebrate when things actually work.
    """

    MESSAGES = [
        "Holy crap, it actually worked! Don't get used to this level of competence.",
        "Success! Time to celebrate with a Pawtucket Patriot!",
        "Nailed it! I'm like a computer genius... for about 5 seconds.",
        "There ya go! I knew I could figure it out eventually.",
        "Boom! Explained like a boss. Peter Griffin, computer expert!",
        "Sweet! That went better than expected. Unlike most things I do.",
        "Victory! Time for a victory dance... or maybe just sit down.",
        "Got it! I'm basically the Bill Gates of explaining stuff.",
    ]

    @staticmethod
    def get_random_message() -> str:
        """
        Returns a random success message.

        Returns:
            str: A random success message
        """
        return random.choice(SuccessMessage.MESSAGES)


class WelcomeMessage:
    """
    Welcome messages for when users start the application.
    """

    MESSAGES = [
        "Welcome to Peter's Command School! Where learning meets... uh... other learning stuff!",
        "Hey there! Ready to learn some Linux? I sure ain't, but let's do this anyway!",
        "Greetings, computer person! Peter Griffin at your service. Sort of.",
        "Welcome! I'm here to explain Linux stuff. Don't expect miracles.",
        "Hey! Ready for some command line wisdom from yours truly?",
    ]

    @staticmethod
    def get_random_message() -> str:
        """
        Returns a random welcome message.

        Returns:
            str: A random welcome message
        """
        return random.choice(WelcomeMessage.MESSAGES)
