# MICROSERVICE ASSESSMENT

The API route to get first 100 jokes from `bash.org.pl` is `/getjokes`

for example :
```
    http://<host-ip>:<host-port>/getjokes
```

the number of jokes can also be updated by append a count parameter to the endpoint's request query

```
    http://<host-ip>:<host-port>/getjokes?count=3
```

Here are the base URLs for each environment



production:  http://52.14.176.88:5002

development:   http://52.14.176.88:5001

release:      http://52.14.176.88:5000