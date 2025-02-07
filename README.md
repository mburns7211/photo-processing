# photo-processing


## Deplyoment
```
sam deploy --guided
```

### After Initial Deployment
*This is to avoid circular dependencies in the sam template*

```
aws s3api put-bucket-notification-configuration --bucket mjburns-raw-photos --notification-configuration '{
  "LambdaFunctionConfigurations": [
    {
      "LambdaFunctionArn": "arn:aws:lambda:us-east-1:911167921393:function:PhotoProcessingFunction",
      "Events": ["s3:ObjectCreated:*"]
    }
  ]
}'

```
