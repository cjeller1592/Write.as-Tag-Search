import writeas

# This is a way to grab the tags from a collection
def retrieveTags(collection):
    c = writeas.NewClient()

    # Choose the collection
    cPosts = c.retrieveCPosts(collection)

    # Grab the collection posts
    posts = cPosts['posts']

    # Creating the list to store the tags
    list = []

    # Embedded for loop: grab the tags for each posts
    # For each unique tag, store it into the list

    for post in posts:
        tags = post['tags']
        for tag in tags:
            list.append(tag)

    return list

# This is way to grab posts with a specific tag
def searchTags(collection, tag):
    c = writeas.NewClient()

    # Choose the collection
    cPosts = c.retrieveCPosts(collection)

    # Grab the collection posts
    posts = cPosts['posts']

    # Creating the list to store the matching tagged posts
    list = []

    # Embedded for loop: grab the tags for each posts
    # For each tag, compare to searched tag and store matches in lists
    for post in posts:
        ptags = post['tags']
        for ptag in ptags:
            if ptag == tag:
                list.append(post)

    # Return list that can be queried: ex. list[0]['title']
    if list == []:
        return 'No posts with the %s tag' % tag

    else:
        return list
