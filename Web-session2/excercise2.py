import excercise1
database = excercise1.connect()
post = database["posts"]
new_post = {
    "title": "Lily",
    "author": "Lxt",
    "content": """
    Roses are red,
    Here's something new.
    Violets are violet,
    They're not blue.
    """
}
post.insert_one(new_post)
