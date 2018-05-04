Welcome to the quick and dirty pangram checker.

*A pangram is defined as sentence, or string or characters, that uses every letter
in a given alphabet (assumed English here) at least once.*

One of the most famous pangram phrases is: The quick brown fox jumps over the lazy dog

# API

This particular pangram checker provides two different api endpoints:

## pangram

Used to check to see if a string of characters is a pangram (superset method).

**URL** : `/api/pangram/{input_string}`

**Method** : `GET`

**Auth required** : NO

### Success Response

Unless there was an error all responses should be successful and return either
True or False.

**Code** : `200 OK`

**Content example**

```json
{
    "pangram": true
}
```

```json
{
    "pangram": false
}
```

## pangram2

Used to check to see if a string of characters is a pangram (alpha character count method).

**URL** : `/api/pangram2/{input_string}`

**Method** : `GET`

**Auth required** : NO

### Success Response

Unless there was an error all responses should be successful and return either True or False.

**Code** : `200 OK`

**Content example**

```json
{
    "pangram": true
}
```

```json
{
    "pangram": false
}
```

# Deployment

To deploy, ensure that you have setup your AWS credentials (see aws configure) and run `chalice deploy`

The output will provide the API Gateway endpoint url.

If you want to run locally you can use `chalice local --port 8080` setting port to whatever if convienent for your environment.

# Usage

`curl "https://someapigwendpoint.amazonaws.com/api/pangram/thequickbrownfoxjumpsoverthelazydog"`
