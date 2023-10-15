class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)
        print(f"Track '{track}' added to the playlist '{self.name}'.")

    def remove_track(self, track):
        if track in self.tracks:
            self.tracks.remove(track)
            print(f"Track '{track}' removed from the playlist '{self.name}'.")
        else:
            print(f"Track '{track}' not found in the playlist '{self.name}'.")

    def show_playlist(self):
        print(f"Playlist '{self.name}':")
        for index, track in enumerate(self.tracks, start=1):
            print(f"{index}. {track}")


class MusicPlayer:
    def __init__(self):
        self.playlists = {}

    def create_playlist(self, name):
        if name not in self.playlists:
            self.playlists[name] = Playlist(name)
            print(f"Playlist '{name}' created.")
        else:
            print(f"Playlist '{name}' already exists.")

    def add_track_to_playlist(self, playlist_name, track):
        if playlist_name in self.playlists:
            self.playlists[playlist_name].add_track(track)
        else:
            print(f"Playlist '{playlist_name}' not found.")

    def remove_track_from_playlist(self, playlist_name, track):
        if playlist_name in self.playlists:
            self.playlists[playlist_name].remove_track(track)
        else:
            print(f"Playlist '{playlist_name}' not found.")

    def show_playlists(self):
        print("Available playlists:")
        for playlist in self.playlists:
            print(f"- {playlist}")


