from cdk_dynamo_table_view import TableViewer
from constructs import Construct
from aws_cdk import (
    CfnOutput,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

from cdk_workshop.hitcounter import HitCounter


class CdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = _lambda.Function(
            self,
            "HelloHandler",
            runtime=_lambda.Runtime.PYTHON_3_10,
            code=_lambda.Code.from_asset("cdk_workshop/lambda"),
            handler="hello.handler",
        )

        hello_with_counter = HitCounter(self, "HelloHitCounter", downstream=my_lambda)

        gateway = apigw.LambdaRestApi(
            self,
            "Endpoint",
            handler=hello_with_counter.handler,
        )

        table_viewer = TableViewer(
            self,
            "ViewHitCounter",
            title="Hello Hits",
            table=hello_with_counter.table,
        )

        # expose urls for health checks
        self.table_viewer_url = CfnOutput(
            self, "TableViewerUrl", value=table_viewer.endpoint
        )
        self.hit_counter_url = CfnOutput(self, "HitCounterUrl", value=gateway.url)
