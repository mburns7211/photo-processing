# photo-processing


## Deplyoment
```
sam deploy --guided
```

### After Initial Deployment
add s3 event to lambda config

## add to lambda layer
```
pip3 install --target layer/python/lib/python3.9/site-packages <PACKAGE> --platform manylinux2014_x86_64 --only-binary=:all: --upgrade   
```