# ECS Service Scale λ

ECS doesn't have away to schedule auto scaling for ECS service. You can use this lambda to schedule event to set desire count for your ECS service.  
This could be used to stop and start your ECS services on schedule.

## How to use
1. `$ git clone https://github.com/XenonLab/aws-ecs-service-scaling-lambda.git` or [download zip](https://github.com/XenonLab/aws-ecs-service-scaling-lambda/archive/master.zip).
2. Deploy to lambda function with your favorite method e.g. copy content of scaling.py to editor or upload zip to S3 bucket
3. Create custom Cloudwatch Event Rule with event defined as Constant (JSON text) and attach it to Lambda
    ```json
    {
       "cluster": "mycluster",
       "service_name": "myservice",
       "service_desired_count": "1"
    }
    ```

4. Configure lambda
  * Runtime: Python
  * Handler: `lambda_function.scale_service`
  * Set & attach `role` to lambda function
  * Minimum role policy
   ```json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents"
          ],
          "Resource": "arn:aws:logs:*:*:*"
        },
        {
          "Effect": "Allow",
          "Action": [
            "ecs:UpdateService"
          ],
          "Resource": "*"
        }
      ]
    }
```

5. Define cloudwatch rule to set schudle for this lambda.



