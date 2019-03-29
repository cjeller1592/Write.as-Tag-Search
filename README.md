# Writeas-Tag-Search
A tool for searching Write.as tags

Sometimes it is tricky to keep track of tags on Write.as, let alone search for them via the API

Here are some functions that can help with that.

**Requirements:** [Write.as API](https://github.com/cjeller1592/Writeas-API)

**TODO:**
- Prevent tags from repeating themselves in retrieveTags results
- [Read.write.as](https://read.write.as) integration

## Retrieving Tags used in a Collection
```
retrieveTags('matt')

# Returns a list of the tags used in a collection

[
'AWP', 'travel', 'FLtoOR', 'trains', 'keto', 'travel', 
'FLtoOR', 'trains', 'amtrak', 'AWP', 'travel', 'FLtoOR', 
'trains', 'AWP', 'personal', 'travel', 'work', 'newyear2019', 'WriteFreely', 
'ReadAs', 'ActivityPub', 'fediverse', 'hashtags', 'fediverse', 
'CamelCase', 'WriteAs', 'tags', 'ActivityPub'
]
```

## Retrieving Posts from a Collection using a Tag
```
searchTags('deaconpatrick', 'WithAbandon')

# Returns a list of posts from a collection that use the tag you are searching

```
