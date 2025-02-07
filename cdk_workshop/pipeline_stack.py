from constructs import Construct
from aws_cdk import (
    Stack,
    aws_codepipeline as codepipeline,
)


class WorkshopPipelineStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        repo = codepipeline.Repository(
            self, "WorkshopRepo", repository_name="WorkshopRepo"
        )
