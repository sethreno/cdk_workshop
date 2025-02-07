from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    assertions
)
from cdk_workshop.hitcounter import HitCounter
import pytest


def test_dynamo_db_table_created():
    stack = Stack()
    HitCounter(
        stack,
        'HitCounter',
        downstream=_lambda.Function(
            stack,
            'TestFunction',
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler='hello.handler',
            code=_lambda.Code.from_asset('cdk_workshop/lambda'),
        ),
    )
    template = assertions.Template.from_stack(stack)
    template.resource_count_is('AWS::DynamoDB::Table', 1)
