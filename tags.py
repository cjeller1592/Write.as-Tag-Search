import writeas
import json

# This is a way to grab the tags from a collection
def retrieveTags(collection):
    c = writeas.NewClient()

    # Choose the collection
    try:
        cPosts = c.retrieveCPosts(collection)

    except Exception as e:
        return 'Nothing! Are you sure this collection exists?'

    # Grab the collection posts
    posts = cPosts['posts']

    # Creating the list to store the tags
    tlist = []

    # Embedded for loop: grab the tags for each posts
    # For each unique tag, store it into the list

    for post in posts:
        tags = post['tags']
        for tag in tags:
            tlist.append(tag)

    if tlist == []:
        return 'No tags found for %s!' % collection
    # Make the list into a dictionary with the items as keys
    # This will automatically remove the duplicates because dicts cant have them
    else:
        tags = list(dict.fromkeys(tlist))
        results = json.dumps(tags)

        return 'Here are the tags for %s: %s' % (collection, results)
