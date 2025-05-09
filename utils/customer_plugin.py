from semantic_kernel.functions import kernel_function

class StrategiesPlugin:
    def __init__(self):
        self.location_key_words = [
            "map won't open", "can't find where I am", "location not visible",
            "nothing is moving", "system seems stuck", "location",
            "current location", "GPS", "allow location permission", "show location",
            "location permission", "device location", "browser settings", "allow location access",
            "reposition", "blue dot", "map marker", "refresh screen"
        ]

    @kernel_function(description="Provide possible solutions for user issues")
    def get_strategies(self, topic: str = "general") -> str:
        for l in self.location_key_words:
            if l in topic:
                return (
                    "Hi there~ No worries, I'm here to help you step by step. It's very normal to feel uncertain when using this feature for the first time.\n"
                    "Regarding your concern about 'can't find the location', it could be that location services haven't been enabled or the screen hasn't displayed correctly. Let's check together.\n"
                    "No need to worry, I'll guide you through it. You mentioned 'can't find where I am', which is usually related to location services.\n"
                    "First, let's check if the location permission is enabled, or if your device has successfully detected your current position.\n"
                    "Please check if your phone allows this website or app to access your location. If you're using an iPhone, go to 'Settings → Safari → Location' and make sure it's set to 'Allow'.\n"
                    "You can also try checking your phone or computer settings to see if location permission is enabled, or choose 'Allow Location' when using the map.\n"
                    "Try pressing 'reposition' or refreshing the page. Do you see a blue dot or small circle on the screen? That represents your current location.\n"
                    "Is there a blue circle on the screen showing your location? If not, let's double-check that your internet and location services are properly enabled.\n"
                    "Looks like the location feature is working again~ You did great! If you run into any more issues, feel free to ask. We're always happy to help.\n"
                    "Great! The location feature should be working fine now~ If you ever need help again, don't hesitate to reach out. We're here for you anytime."
                )
        return (
            "This is a common issue. I recommend trying to restart the system, check your network connection, or see if there's a software update available. "
            "If the issue persists, feel free to contact us anytime."
        )
