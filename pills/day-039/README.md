# [Python daily pills] Day 039 - Python's built-in HTTP server

Python has a HTTP server built into the standard library. This is super handy for previewing websites.

```python
# Python 3.x
$ python3 -m http.server

# Python 2.x
$ python -m SimpleHTTPServer 8000
```

> Note: By default, this will run the contents of the directory on a local web server, on port 8000. You can go to this server by going to the URL [localhost:8000](localhost:8000) in your web browser.

## References

- The [official python docs](https://docs.python.org/3/library/http.server.html).
- A great [mozilla article](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server) about testing local files vs. remote files.
