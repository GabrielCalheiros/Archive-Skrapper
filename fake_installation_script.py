import random
import time

# Generates a sleep for a random time between min_time and max_time seconds
def random_sleep(min_time=0.001, max_time=0.7):
    time.sleep(random.uniform(min_time, max_time))

def main():
    # Choose a random number for the phrases
    number = round(random.uniform(1, 100))

    phrase_A = [
        f"Merging {number} branches",
        f"Downloading {number} packages",
        f"Resolving dependencies",
        f"Compiling {number} source code files",
        f"Setting up environment",
        f"Fetching latest updates", 
        f"Synchronizing {number} files",
        f"Installing libraries",
        f"Checking disk space",
        f"Initializing setup",
        f"Validating checksums",
        f"Updating configuration",
        f"Applying {number} patches",
        f"Preparing for final installation",
        f"Unpacking {number} archives",
        f"Optimizing {number} settings",
        f"Backing up {number}mb of data",
        f"Creating system restore point",
        f"Cleaning temporary files",
        f"Verifying digital signatures"
    ]

    phrase_B = [
        " with the cloud repository",
        " from the central server",
        " to the local system",
        " to the user directory",
        " from the secure network",
        " with the latest updates",
        " for optimized performance",
        " using secure protocols",
        " for user-specific settings",
        " to the specified path",
        " from the mirror site",
        " with administrator privileges",
        " for compatibility",
        " for enhanced security",
        " from the trusted source",
        " to ensure integrity",
        " to maximize efficiency",
        " to prevent data loss",
        " for system stability",
        " for improved functionality"
    ]

    phrase_C = [
        " to configure files and folders for execution...",
        " to complete the installation process...",
        " to finalize the setup...",
        " to ensure all dependencies are met...",
        " to optimize runtime performance...",
        " to prepare the environment...",
        " to validate the configuration...",
        " to initialize the application...",
        " to set up user preferences...",
        " to verify installation integrity...",
        " to check system compatibility...",
        " to update the registry...",
        " to clean up temporary files...",
        " to reboot the system if necessary...",
        " to enable new features...",
        " to confirm changes...",
        " to secure the installation...",
        " to patch vulnerabilities...",
        " to complete the final steps...",
        " to finalize settings adjustments..."
    ]

    status_phrases = [
        "Please wait...",
        "Almost done...",
        "Just a moment...",
        "Processing...",
        "Loading...",
        "Finishing up...",
        "Applying changes...",
        "Completing installation...",
        "Finalizing...",
        "Executing final steps...",
        "Completing setup...",
        "Optimizing...",
        "Verifying...",
        "Upgrading...",
        "Checking...",
        "Setting up...",
        "Installing...",
        "Preparing...",
        "Preparing...",
        "Initializing...",
        "Setting up...",
    ]

    # Generate a random phrase using different templates
    complete_phrase = random.choice(phrase_A) + random.choice(phrase_B) + random.choice(phrase_C)
    print(complete_phrase)

    # Randomly insert a status phrase
    if random.random() < 0.2:  # 30% chance to insert a status phrase
        print(random.choice(status_phrases))

    # Introduce a random sleep after printing the phrase
    random_sleep()

if __name__ == "__main__":
    # Randomly determine the number of actions between 20 and 60
    number_of_actions = random.randint(100, 1000)
    
    for i in range(number_of_actions):
        main()
        # Add another random sleep between actions to vary the pace
        random_sleep(0.05, 1.5)
