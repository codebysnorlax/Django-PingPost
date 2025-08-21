### Functional Requirements

- User Registration: Users can create an account with username, email, and password.
- Authentication: Users can log in and log out using Django auth.
- Create Tweet: Authenticated users can create a tweet with text and optional image.
- Edit Tweet: Authenticated users can edit only their own tweets.
- Delete Tweet: Authenticated users can delete only their own tweets.
- List Tweets: Anyone can view the reverse-chronological list of tweets.
- Uploads: Images are persisted to `media/photos/` and served in development.
