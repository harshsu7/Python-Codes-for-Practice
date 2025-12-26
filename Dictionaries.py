playlist = {}

def createPlaylist():
    global playlist
    vibes = ["happy", "sad", "energetic", "relaxed"]

    happy_songs = [
        "Let's Go Crazy by Prince",
        "I Got You (I Feel Good) by James Brown",
        "Good as Hell by Lizzo"
    ]

    sad_songs = [
        "Let Her Go",
        "Take Me to Church",
        "Someone Like Me"
    ]

    energetic_songs = [
        "Brazil La La La",
        "Waka Waka by Shakira",
        "Ms. Jackson by B.O.B"
    ]

    relaxed_songs = [
        "Perfect by Ed Sheeran",
        "Fly Me to the Moon",
        "Beautiful Girl by Sean Kingston"
    ]

    playlist = dict(zip(
        vibes,
        [happy_songs, sad_songs, energetic_songs, relaxed_songs]
    ))


def displayPlaylist():
    global playlist
    mood = input("How are you feeling today? Enter your mood/genre: ").lower()

    if mood in playlist:
        print("\nHere's your genre playlist:")
        for song in playlist[mood]:
            print("-", song)
    else:
        print("Sorry, the mood is not available in the playlist.")


def updatePlaylist():
    global playlist
    mood = input("Choose genre you want to update or add: ").lower()

    if mood in playlist:
        print("This mood exists. Add your own songs to update it.")
    else:
        print("This mood is new. Add songs for the new genre.")

    songs = input(
        "Enter songs for this genre (separate by commas): "
    ).split(",")

    # clean extra spaces
    songs = [song.strip() for song in songs]

    playlist[mood] = songs
    print("The mood and its songs have been added/updated.")


def showAll():
    global playlist

    print("\nAll genres:")
    for mood in playlist.keys():
        print("-", mood)

    print("\nAll songs:")
    for songs in playlist.values():
        for song in songs:
            print("-", song)

    print("\nAll moods with songs:")
    for mood, songs in playlist.items():
        print(mood, ":", songs)


def removeVibes():
    global playlist
    vibesToRemove = input("Enter the genre you want to remove: ").lower()

    if vibesToRemove in playlist:
        playlist.pop(vibesToRemove)
        print("Genre and its songs have been removed.")
    else:
        print("Genre not found in the playlist.")


# Example run
createPlaylist()
showAll()