import random


class LoadingMessage:
    """
    Class to store loading messages for the Peter Explains CLI.
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
    ]

    @staticmethod
    def get_random_message() -> str:
        """
        Returns a random message from the available messages.

        Returns:
            str: A random message.
        """
        return random.choice(LoadingMessage.MESSAGES)


class ErrorMessage:
    """
    Class to store error messages for the Peter Explains CLI.
    """

    MESSAGES = [
        "Aw crap, somethin' broke. Typical. Maybe Meg stepped on the keyboard again.",
        "Hey, if this thing gives ya the wrong answer, don't blame me. I'm just the idiot typin' stuff in.",
        "Alright, this might take longer than I thought. You got any beer in the fridge?",
        "Ugh, somethin' ain't right. Maybe I shoulda paid more attention to that computer class in high school.",
        "Aw jeez, I think I broke it. Don't tell Lois, she'll make me fix it.",
        "I swear, this thing's got more bugs than the Griffin house. And that's sayin' somethin'.",
    ]

    @staticmethod
    def get_random_message() -> str:
        """
        Returns a random error message from the list of error messages.

        Returns:
            str: A random error message.
        """
        return random.choice(ErrorMessage.MESSAGES)
