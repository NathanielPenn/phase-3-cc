class Viewer:

    def __init__(self, username):
        self.username = username

        self.reviewers = []
        self.reviews = []
        pass

    @property
    def username(self):
        return self._username
        pass
    
    @username.setter
    def username(self, username):
        if type(username) == str and 6 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("Username must be a unique string between 6 and 16 characters long")
        
        pass

    def reviewed_movie(self, movie):
        pass

    def rate_movie(self, movie, rating):
        from review import Review
        Review(self, movie, rating)
        pass

    